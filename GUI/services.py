from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox

from GUI.trim_dialog import TrimDialog
from Model.project import Project


def editor_concat(parent, fragment_index):
    fragments = [x.content for x in parent.session.project.active_fragments]
    choice, ok = QInputDialog.getItem(parent, 'Склеить', 'Выбирите фрагмент, с которым нужно склеить текущий',
                                      fragments)
    if ok:
        next_fragment_index = fragments.index(choice)
        if next_fragment_index == fragment_index:
            msg = QMessageBox()
            msg.setText("Ошибка")
            msg.setInformativeText('Нельзя склеить элемент с самим собой')
            msg.exec_()
        else:
            parent.session.project.concat(fragment_index, next_fragment_index)

def editor_trim(parent, fragment_index):
    a = TrimDialog(parent)
    a.exec()
    results = a.getInputs()
    if results[0] == '' or results[1] == '':
        return
    parent.session.project.trim(fragment_index, results[0], results[1])

def menu_new(parent):
    name, ok = QInputDialog.getText(parent, "Новый проект", "Введите название")
    if ok:
        parent.session.project = Project(name)

def editor_add_content(parent, fragment_index):
    parent.session.project.player.set_content(parent.session.project.active_fragments[fragment_index])
    parent.audio_name.setText(QUrl(parent.session.project.player.fragment_name.content).fileName())
    parent.seconds = parent.session.project.player.seconds
    parent.duration_text.setText(f'0:00 / {parent.session.project.player.duration}')

def editor_change_speed(parent, fragment_index):
    ratio, ok = QInputDialog.getDouble(parent, "Изменение скорости", "Введите коэфицент")
    if ok:
        parent.session.project.change_speed(fragment_index, float(ratio))

def menu_export_file(parent):
    path = QFileDialog.getSaveFileUrl(parent, caption="Сохранить как", filter=(".wav"), )[0].path()
    if path == '':
        return
    parent.session.project.export_as_file(path + ".wav")

def menu_import_file(parent):
    path = QFileDialog.getOpenFileUrl(parent, caption="Импортировать")

    s = path[0].path()[1:]
    if s != '':
        parent.session.project.import_file(s)

def menu_save_as_file(parent):
    url = QFileDialog.getSaveFileUrl(parent, caption="Сохранить как...", filter=".artl")
    path = url[0].path() + '.artl'
    parent.session.project.path = path
    parent.session.project.name = url[0].fileName()
    data = parent.session.project.pack()
    with open(path[1:], 'w') as f:
        for line in data:
            f.write(line + '\n')

def menu_save_file(parent):
    if parent.session.project.path == "":
        parent.menu_save_as_file()
    else:
        data = parent.session.project.pack()
        with open(parent.session.project.path, 'w') as f:
            for line in data:
                f.write(line)

def menu_open_file(parent):
    url = QFileDialog.getOpenFileUrl(parent, caption="Открыть")
    path = url[0].path()[1:]
    if path != '':
        with open(path, 'r') as f:
            lines = f.readlines()
            parent.session.project = Project.unpack(lines, url[0].fileName(), path)

def stop(parent):
    parent.is_paused = True
    parent.session.player_stop()