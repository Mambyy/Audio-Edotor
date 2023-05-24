from math import floor

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import ffmpeg

class Player:
    def __init__(self):
        self.fragment_name = None
        self.duration = None
        self.seconds = None
        self.player = QMediaPlayer()
        self.content = QMediaContent()

    def set_content(self, content):
        self.duration = content.duration
        self.seconds = content.seconds
        self.content = QMediaContent(QUrl.fromLocalFile(content.content))
        self.player.setMedia(self.content)
        self.fragment_name = content

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume_level):
        self.player.setVolume(volume_level)

    def set_position(self, position):
        self.player.setPosition(self.player.duration() * position / 1000)

    def get_duration(self):
        return self.player.duration()

    def get_progress(self):
        if self.player.duration() != 0:
            return self.player.position() / self.player.duration()
        else:
            return 0

    @staticmethod
    def duration_to_str(duration):
        return f'{floor(duration / 60)}:{"0" if floor(duration % 60) < 10 else ""}{floor(duration % 60)}'
