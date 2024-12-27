from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel, QHBoxLayout, QStackedWidget, QFrame
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont


class InfoButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/info.png")) 
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


class InfoDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Info")
        self.setFixedSize(900, 600)

        # Основной layout
        main_layout = QVBoxLayout()

        # Основной контейнер для карусели и стрелок
        carousel_layout = QHBoxLayout()

        # Кнопка "Предыдущая"
        self.prev_button = QPushButton()
        self.prev_button.setFixedSize(50, 50)
        self.prev_button.setIcon(QIcon("resources/icons/left.png")) 
        self.prev_button.setIconSize(QSize(40, 40))
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.2);
                           border-radius: 25px;
            }
        """)
        self.prev_button.clicked.connect(self.show_previous_card)
        carousel_layout.addWidget(self.prev_button)

        # Карусель с рамкой
        self.stacked_widget = QStackedWidget()
        frame = QFrame()
        frame.setFixedSize(750, 425)
        frame.setStyleSheet("""
            QFrame {
                border: 1px solid silver;
                border-radius: 15px;
                background-color: rgba(0, 0, 0, 0);
            }
        """)
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(self.stacked_widget)
        frame.setLayout(frame_layout)
        carousel_layout.addWidget(frame)

        # Кнопка "Следующая"
        self.next_button = QPushButton()
        self.next_button.setFixedSize(50, 50)
        self.next_button.setIcon(QIcon("resources/icons/right.png")) 
        self.next_button.setIconSize(QSize(40, 40))
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.2);
                           border-radius: 25px;
            }
        """)
        self.next_button.clicked.connect(self.show_next_card)
        carousel_layout.addWidget(self.next_button)

        # Добавляем карусель в основной layout
        main_layout.addLayout(carousel_layout)

        # Добавляем карточки в карусель
        self.add_card("BED\n-\nYour giude to a better life\n\n\n\n\nThis is the list of updates from the first version to the current\n\n\n\n\n\n© 2024-2025 Alexandrow")
        self.add_card("BED\n-\n1.1\n\n\n1. Info cards\n\n2. Notes\n\n3. Fixed some bugs\n\n\n\n© 2024-2025 Alexandrow")
        self.add_card("BED\n-\n1.0\n\n\n1. Habits tracker\n\n2. Tasks tracker\n\n3. About\n\n4. Design\n\n\n\n© 2024-2025 Alexandrow")

        self.setLayout(main_layout)


    def add_card(self, text):
        """Добавляет новую карточку в карусель."""
        card = QLabel(text)
        card.setAlignment(Qt.AlignCenter)
        card.setFont(QFont("Georgia", 14))
        card.setWordWrap(True)
        self.stacked_widget.addWidget(card)


    def show_next_card(self):
        """Показывает следующую карточку."""
        current_index = self.stacked_widget.currentIndex()
        if current_index < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(current_index + 1)


    def show_previous_card(self):
        """Показывает предыдущую карточку."""
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(current_index - 1)
