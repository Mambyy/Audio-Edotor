from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut

from GUI import services


def init_shortcuts(parent):
    parent.shortcut_create = QShortcut(QKeySequence('Ctrl+N'), parent)
    parent.shortcut_create.activated.connect(parent.execute(services.menu_new))

    parent.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), parent)
    parent.shortcut_open.activated.connect(parent.execute(lambda: services.menu_open_file(parent)))

    parent.shortcut_save = QShortcut(QKeySequence('Ctrl+S'), parent)
    parent.shortcut_save.activated.connect(parent.execute(lambda: services.menu_save_file(parent)))

    parent.shortcut_save_as = QShortcut(QKeySequence('Ctrl+Shift+S'), parent)
    parent.shortcut_save_as.activated.connect(parent.execute(lambda: services.menu_save_as_file(parent)))

    parent.shortcut_undo = QShortcut(QKeySequence('Ctrl+Z'), parent)
    parent.shortcut_undo.activated.connect(parent.execute(parent.session.project.undo))

    parent.shortcut_redo = QShortcut(QKeySequence('Ctrl+Y'), parent)
    parent.shortcut_redo.activated.connect(parent.execute(parent.session.project.redo))

    parent.shortcut_import_media = QShortcut(QKeySequence('Ctrl+I'), parent)
    parent.shortcut_import_media.activated.connect(parent.execute(lambda: services.menu_import_file(parent)))

    parent.shortcut_export_media = QShortcut(QKeySequence('Ctrl+E'), parent)
    parent.shortcut_export_media.activated.connect(parent.execute(lambda: services.menu_export_file(parent)))

    parent.shortcut_play = QShortcut(Qt.Key_Space, parent)
    parent.shortcut_play.activated.connect(__play_shortcut)

    parent.shortcut_stop = QShortcut(QKeySequence('Shift+Space'), parent)
    parent.shortcut_stop.activated.connect(lambda: services.stop(parent))

def __play_shortcut(parent):
    if parent.is_paused:
        parent.session.player_play()
    else:
        parent.session.player_pause()

    parent.is_paused = not parent.is_paused