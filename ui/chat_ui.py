from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont


class ChatButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)  # Фиксированный размер кнопки
        self.setIcon(QIcon("resources/icons/chat.png"))  # Иконка чата
        self.setIconSize(QSize(50, 50))  # Размер иконки
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.1);
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.2);
            }
        """)


class ChatDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Chat")
        self.setFixedSize(1100, 625)

        layout = QVBoxLayout()

        self.label = QLabel("Hi")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.label.setFont(font)

        layout.addWidget(self.label)

        self.setLayout(layout)
