import math
import threading

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QWidget

from GUI import services
from GUI.jump_slider import QJumpSlider
from Model.ffmeg_editor import convert_seconds_to_time


def get_player_layout(parent):
    title_layout = QHBoxLayout()
    title_layout.addLayout(get_player_buttons_layout(parent))
    title_layout.addWidget(parent.audio_name)
    title_layout.addWidget(get_global_volume_slider(parent))

    slider_layuot = QHBoxLayout()
    slider_layuot.addWidget(parent.duration_text)
    slider_layuot.addWidget(get_progress_slider(parent))
    slider_layuot.addWidget(parent.length_text)

    player_layout = QVBoxLayout()
    player_layout.addLayout(title_layout)
    player_layout.addLayout(slider_layuot)


    player_widget = QWidget()
    player_widget.setLayout(player_layout)

    return player_widget

def get_player_buttons_layout(parent):
    play_button = QPushButton()
    play_button.setIcon(QIcon('GUI/textures/play_btn.png'))
    play_button.setFixedSize(45, 45)
    play_button.clicked.connect(lambda: parent.session.player_play())
    pause_button = QPushButton('⏸')
    pause_button.setFixedSize(45, 45)
    pause_button.clicked.connect(lambda: parent.session.player_pause())
    stop_button = QPushButton('⏹')
    stop_button.setFixedSize(45, 45)
    stop_button.clicked.connect(lambda: services.stop(parent))

    main_buttons_layout = QHBoxLayout()
    main_buttons_layout.addWidget(pause_button)
    main_buttons_layout.addWidget(play_button)
    main_buttons_layout.addWidget(stop_button)

    return main_buttons_layout

def get_global_volume_slider(parent):
    global_volume_slider = QJumpSlider(Qt.Horizontal)
    global_volume_slider.setFixedSize(150, 15)

    global_volume_slider.setMinimum(0)
    global_volume_slider.setMaximum(100)
    global_volume_slider.setSingleStep(1)
    global_volume_slider.setValue(100)

    global_volume_slider.valueChanged.connect(parent.session.player_set_volume)

    return global_volume_slider

def get_progress_slider(parent):
    parent.progress_slider = QJumpSlider(Qt.Horizontal)
    parent.progress_slider.setFixedSize(650, 50)

    parent.progress_slider.setMinimum(0)
    parent.progress_slider.setMaximum(1000)

    parent.progress_slider.setSingleStep(1)
    parent.progress_slider.setValue(0)

    parent.progress_slider.set_run_on_click_function(parent.session.player_set_position)

    return parent.progress_slider

def update_progress(parent):
    threading.Timer(0.01, lambda: update_progress(parent)).start()
    progress = parent.session.project.player.get_progress()

    if parent.session.project.player.fragment_name is not None:
        if parent.seconds is not None:
            parent.duration_text.setText(convert_seconds_to_time(math.floor(parent.seconds * progress)))
            parent.length_text.setText(convert_seconds_to_time(math.floor(parent.seconds)))

    parent.progress_slider.setValue(progress * parent.progress_slider.maximum())