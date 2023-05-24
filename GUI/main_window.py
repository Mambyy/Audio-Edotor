from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import  QHBoxLayout, QWidget, QVBoxLayout, QMainWindow, QLabel

from GUI import shirtcuts, menubar, table, player


class MainWindow(QMainWindow):
    def __init__(self, session):
        super().__init__()
        self.session = session

        self.audio_name = QLabel()
        self.audio_name.setText('-')
        self.audio_name.setFont(QFont('Arial', 20))
        self.duration_text = QLabel()
        self.duration_text.setText('0:00')
        self.duration_text.setFont(QFont('Arial', 14))
        self.length_text = QLabel()
        self.length_text.setText('0:00')
        self.length_text.setFont(QFont('Arial', 14))
        self.is_paused = True
        self.seconds = None
        self.setFixedSize(QSize(800, 500))
        self.setStyleSheet("background-color: #3C3F41;")

        self.refresh()
        shirtcuts.init_shortcuts(self)
        menubar.create_menubar(self)

    def refresh(self):
        self.setWindowTitle(self.session.project.name + " - AudioEditor")

        general_layout = QVBoxLayout()
        general_layout.addWidget(player.get_player_layout(self))
        general_layout.addWidget(table.get_table_layout(self))
        container = QWidget()
        container.setLayout(general_layout)
        self.setCentralWidget(container)

        player.update_progress(self)

    def execute(self, func_to_execute):
        def func():
            func_to_execute()
            self.refresh()
        return func
