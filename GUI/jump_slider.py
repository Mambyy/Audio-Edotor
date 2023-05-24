from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, \
    QStyle


class QJumpSlider(QSlider):
    def __init__(self, parent=None):
        super(QJumpSlider, self).__init__(parent)
        self.run_on_click = None

    def mousePressEvent(self, event):
        self.mouse_event(event)

    def mouseMoveEvent(self, event):
        self.mouse_event(event)

    def mouse_event(self, event):
        self.setValue(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(),
                                                     event.x() if self.orientation() == Qt.Horizontal else -event.y(),
                                                     self.width() if self.orientation() == Qt.Horizontal
                                                     else self.height()))

        if self.run_on_click is not None:
            self.run_on_click(self.value())

    def set_run_on_click_function(self, function):
        self.run_on_click = function
