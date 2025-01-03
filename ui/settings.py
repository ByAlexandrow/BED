from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont


class SettingsButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/settings.png")) 
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


class SettingsDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Settings")
        self.setFixedSize(900, 600)

        layout = QVBoxLayout()

        self.settings_label = QLabel("Settings")
        self.settings_label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.settings_label.setFont(font)

        layout.addWidget(self.settings_label)

        self.setLayout(layout)
