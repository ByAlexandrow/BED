from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


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
        self.setFixedSize(900, 600)

        layout = QVBoxLayout()
