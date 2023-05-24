from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QFormLayout


class TrimDialog(QDialog):
    # T0D0 Сделать нормальный ползунок, а не два поля
    def __init__(self, parent):
        super().__init__(parent)
        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)
        layout.addRow("Начало", self.first)
        layout.addRow("Конец", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return self.first.text(), self.second.text()