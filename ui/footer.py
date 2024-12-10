from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Footer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()


    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Добавляем растягивающийся элемент слева
        layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Создаем метку для подписи
        self.footer_label = QLabel("Better Every Day")
        self.footer_label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 12)
        self.footer_label.setFont(font)

        # Добавляем метку в макет
        layout.addWidget(self.footer_label)

        # Добавляем растягивающийся элемент справа
        layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Устанавливаем макет для виджета
        self.setLayout(layout)
