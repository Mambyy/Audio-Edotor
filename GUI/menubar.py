from PyQt5.QtWidgets import QWidgetAction

from GUI import services


def create_menubar(parent):
    menu_bar = parent.menuBar()

    file_menu = menu_bar.addMenu("Файл")

    new_file = QWidgetAction(parent)
    new_file.setText("Создать")
    new_file.triggered.connect(parent.execute(services.menu_new))
    file_menu.addAction(new_file)

    open_file = QWidgetAction(parent)
    open_file.setText("Открыть")
    open_file.triggered.connect(parent.execute(lambda: services.menu_open_file(parent)))
    file_menu.addAction(open_file)

    save_file = QWidgetAction(parent)
    save_file.setText("Сохранить")
    save_file.triggered.connect(parent.execute(lambda: services.menu_save_file(parent)))
    file_menu.addAction(save_file)

    save_as_file = QWidgetAction(parent)
    save_as_file.setText("Сохранить как")
    save_as_file.triggered.connect(parent.execute(lambda: services.menu_save_as_file(parent)))
    file_menu.addAction(save_as_file)

    file_menu.addSeparator()

    import_file = QWidgetAction(parent)
    import_file.setText("Импорт медиа")
    import_file.triggered.connect(parent.execute(lambda: services.menu_import_file(parent)))
    file_menu.addAction(import_file)

    export_file = QWidgetAction(parent)
    export_file.setText("Экспорт медиа")
    export_file.triggered.connect(parent.execute(lambda: services.menu_export_file(parent)))
    file_menu.addAction(export_file)

    edit_menu = menu_bar.addMenu("Правка")

    undo = QWidgetAction(parent)
    undo.setText("Отменить")
    undo.triggered.connect(parent.execute(parent.session.project.undo))
    edit_menu.addAction(undo)
    redo = QWidgetAction(parent)
    redo.setText("Повторить")
    redo.triggered.connect(parent.execute(parent.session.project.redo))
    edit_menu.addAction(redo)