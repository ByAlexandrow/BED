from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize


class TopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(1)

        # Верхний ряд с кнопками и названием
        top_layout = QHBoxLayout()

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
        self.about_button.setIcon(QIcon("resources/icons/about.png"))
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

        top_layout.addWidget(self.account_button)
        top_layout.addWidget(self.app_name_label)
        top_layout.addWidget(self.about_button)

        main_layout.addLayout(top_layout)

        # Нижний ряд с описанием
        bottom_layout = QHBoxLayout()

        self.app_description_label = QLabel("Better Every Day")
        self.app_description_label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.app_description_label.setFont(font)

        bottom_layout.addWidget(self.app_description_label)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)
