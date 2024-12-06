# ui/footer.py
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy

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
        self.label = QLabel("© 2024-2025 Alexandrow")
        self.label.setStyleSheet("color: white; font-size: 12px;")

        # Добавляем метку в макет
        layout.addWidget(self.label)

        # Добавляем растягивающийся элемент справа
        layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Устанавливаем макет для виджета
        self.setLayout(layout)
