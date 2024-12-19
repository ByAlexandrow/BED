from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class NewsChatDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - About")
        self.setFixedSize(550, 250)

        layout = QVBoxLayout()

        self.label = QLabel("Hi\nThis letter is for you\n\nUse this app and join my club\nTry to be better than you are\n\nPROGRESS\nor\nDIE\n\nI'll be in touch with you soon")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.label.setFont(font)

        layout.addWidget(self.label)

        self.setLayout(layout)
