import random

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QApplication
from PySide6.QtGui import QFont, QCursor
from PySide6.QtCore import Qt, QTimer, QRect


class Dialog(QDialog):
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

        self.label.mousePressEvent = self.on_label_click

    
    def on_label_click(self, event):
        cursor = QCursor()
        cursor_position = cursor.pos()
        text = self.label.text()
        if "DIE" in text:
            self.label.setText(text.replace("DIE", ""))
            self.die_explosion()
    

    def die_explosion(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        for _ in range(350):
            label = QLabel("DIE", self)
            label.setFont(QFont("Arial", 25, QFont.Bold))
            label.setStyleSheet("color: red;")
            label.move(random.randint(0, screen_geometry.width()), random.randint(0, screen_geometry.height()))
            label.show()
        QTimer.singleShot(2000, self.shutdown)


    def shutdown(self):
        QApplication.quit()
