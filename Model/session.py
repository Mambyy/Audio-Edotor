from PyQt5.QtWidgets import QFileDialog

from Model.project import Project


class Session:
    def __init__(self):
        self.project = Project("untitled")

    def player_play(self):
        self.project.player.play()

    def player_pause(self):
        self.project.player.pause()

    def player_stop(self):
        self.project.player.stop()

    def player_set_volume(self, volume):
        self.project.player.set_volume(volume)

    def player_set_position(self, position):
        self.project.player.set_position(position)
