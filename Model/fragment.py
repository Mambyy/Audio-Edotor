from Model import ffmeg_editor
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent


class Fragment:
    last_id = 0

    def __init__(self, content):
        self.id = Fragment.last_id
        Fragment.last_id += 1

        self.length = 0
        self.content = content
        self.duration = ffmeg_editor.get_duration(content)
        self.seconds = ffmeg_editor.get_length(content)

    def __eq__(self, other):
        return self.id == other.id
