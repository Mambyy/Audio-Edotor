import sys

from PyQt5.QtWidgets import QApplication

from GUI.main_window import MainWindow
from Model.session import Session

if __name__ == "__main__":
    app = QApplication(sys.argv)
    session = Session()

    window = MainWindow(session)
    window.show()

    app.exec()
