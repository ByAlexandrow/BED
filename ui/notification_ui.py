from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont


class NotificationButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/notification.png")) 
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


class NotificationDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Work Rest Balance")
        self.setFixedSize(1100, 625)

        layout = QVBoxLayout()

        self.label = QLabel("Hi\nWrite me if something works wrong or even doesn't work\nYou can do it here\n")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.label.setFont(font)

        self.social_label = QLabel("Or you can write me here:\n")
        self.social_label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.social_label.setFont(font)

        layout.addWidget(self.label)
        layout.addWidget(self.social_label)

        self.setLayout(layout)
