from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont


class AchievementsButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/achievements.png")) 
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


class AchievementsDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Achievements")
        self.setFixedSize(500, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Achievements")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.label.setFont(font)

        layout.addWidget(self.label)

        self.setLayout(layout)
