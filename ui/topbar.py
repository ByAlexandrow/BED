from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize


class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()


    def init_ui(self):
        main_layout = QHBoxLayout()
        main_layout.setSpacing(1)

        # Создание кнопок и установка размеров
        self.account_button = QPushButton()
        self.account_button.setFixedSize(90, 50)
        self.account_button.setIcon(QIcon("resources/icons/account.png"))
        self.account_button.setIconSize(QSize(40, 40))
        self.account_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)

        self.app_name_label = QLabel("BED")
        self.app_name_label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 19, QFont.Bold)
        self.app_name_label.setFont(font)

        self.about_button = QPushButton()
        self.about_button.setFixedSize(90, 50)
        self.about_button.setIcon(QIcon("resources/icons/news_chat.png"))
        self.about_button.setIconSize(QSize(40, 40))
        self.about_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)

        main_layout.addWidget(self.account_button)
        main_layout.addWidget(self.app_name_label)
        main_layout.addWidget(self.about_button)

        self.setLayout(main_layout)
