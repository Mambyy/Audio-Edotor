from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem

from GUI import services



def get_table_layout(parent):
    table = QTableWidget()
    table.setFixedSize(780, 300)
    rows_count = len(parent.session.project.active_fragments)
    table.setColumnCount(3)
    table.setRowCount(rows_count)
    table.setColumnWidth(0, 370)
    table.setColumnWidth(1, 60)
    table.setColumnWidth(2, 320)

    table.setHorizontalHeaderLabels(["Название", "Длина", "Действия"])
    for i in range(rows_count):
        add_table_row(parent, table, i)

    return table

def add_table_row(parent, table, i):
    table.setRowHeight(i, 50)
    name = QUrl(parent.session.project.active_fragments[i].content).fileName()
    table.setItem(i, 0, QTableWidgetItem(name))
    length = parent.session.project.active_fragments[i].duration
    table.setItem(i, 1, QTableWidgetItem(length))
    tools_panel = QHBoxLayout()

    delete_button = QPushButton('⌫')
    delete_button.clicked.connect(parent.execute(lambda: parent.session.project.delete(i)))
    tools_panel.addWidget(delete_button)
    speed_button = QPushButton('⏩')
    speed_button.clicked.connect(parent.execute(lambda: services.editor_change_speed(parent, i)))
    tools_panel.addWidget(speed_button)
    glue_button = QPushButton('G')
    glue_button.clicked.connect(parent.execute(lambda: services.editor_concat(parent, i)))
    tools_panel.addWidget(glue_button)
    split_button = QPushButton('✂')
    split_button.clicked.connect(parent.execute(lambda: services.editor_trim(parent, i)))
    tools_panel.addWidget(split_button)
    clone_button = QPushButton('C')
    clone_button.clicked.connect(parent.execute(lambda: parent.session.project.clone(i)))
    tools_panel.addWidget(clone_button)
    up_button = QPushButton('↑')
    up_button.clicked.connect(parent.execute(lambda: parent.session.project.up(i)))
    tools_panel.addWidget(up_button)
    down_button = QPushButton('↓')
    down_button.clicked.connect(parent.execute(lambda: parent.session.project.down(i)))
    tools_panel.addWidget(down_button)
    play_button = QPushButton('⏏')
    play_button.clicked.connect(parent.execute(lambda: services.editor_add_content(parent, i)))
    tools_panel.addWidget(play_button)

    tools_panel_widget = QWidget()
    tools_panel_widget.setLayout(tools_panel)
    table.setCellWidget(i, 2, tools_panel_widget)