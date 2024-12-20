from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtGui import QFont, QIcon, QDesktopServices
from PySide6.QtCore import Qt, QUrl, QSize


class NewsChatDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - About")
        self.setFixedSize(550, 250)

        layout = QVBoxLayout()

        self.label = QLabel("Use this app and join my club\nTry to be better than you are\n\nPROGRESS\nor\nDIE\n\nI'll be in touch with you soon")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.label.setFont(font)

        layout.addWidget(self.label)

        layout.addSpacing(20)

        # Горизонтальный макет для иконок социальных сетей
        socials_layout = QHBoxLayout()
        socials_layout.addStretch()

        # Кнопка Telegram
        self.telegram_button = QPushButton()
        self.telegram_button.setIcon(QIcon("resources/icons/telegram.png"))
        self.telegram_button.setIconSize(QSize(40, 40))
        self.telegram_button.setFixedSize(50, 50)
        self.telegram_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.telegram_button.clicked.connect(lambda: self.open_url("https://t.me/By_Alexandrow"))
        socials_layout.addWidget(self.telegram_button)

        # Кнопка ВКонтакте
        self.vk_button = QPushButton()
        self.vk_button.setIcon(QIcon("resources/icons/vk.png"))
        self.vk_button.setIconSize(QSize(40, 40))
        self.vk_button.setFixedSize(50, 50)
        self.vk_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.vk_button.clicked.connect(lambda: self.open_url("https://vk.com/egorka.aleks"))
        socials_layout.addWidget(self.vk_button)

        # Кнопка GitHub
        self.github_button = QPushButton()
        self.github_button.setIcon(QIcon("resources/icons/github.png"))
        self.github_button.setIconSize(QSize(40, 40))
        self.github_button.setFixedSize(50, 50)
        self.github_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.github_button.clicked.connect(lambda: self.open_url("https://github.com/ByAlexandrow"))
        socials_layout.addWidget(self.github_button)

        socials_layout.addStretch()  # Растягивающийся элемент для центрирования
        layout.addLayout(socials_layout)

        self.setLayout(layout)


    def open_url(self, url):
        """Открывает URL в браузере."""
        QDesktopServices.openUrl(QUrl(url))
