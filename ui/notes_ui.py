from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont


class NotesButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/notes.png")) 
        self.setIconSize(QSize(40, 40))
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.1);
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.2);
            }
        """)


class NotesDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Notes")
        self.setFixedSize(900, 600)

        layout = QVBoxLayout()

        self.notes_label = QLabel("Notes")
        self.notes_label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.notes_label.setFont(font)

        layout.addWidget(self.notes_label)

        self.setLayout(layout)
