from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


class NotesButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/notes.png")) 
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


class NotesDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Notes")
        self.setFixedSize(900, 600)

        # Основной макет
        self.layout = QVBoxLayout()

        # Создаем футер
        footer_layout = QHBoxLayout()
        footer_widget = QWidget()
        footer_widget.setLayout(footer_layout)

        # Кнопка "Добавить заметку"
        self.add_notes_button = QPushButton()
        self.add_notes_button.setFixedSize(100, 30)
        self.add_notes_button.setIcon(QIcon("resources/icons/add.png"))
        self.add_notes_button.setIconSize(QSize(30, 30))
        self.add_notes_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.add_notes_button.clicked.connect(self.add_notes_widget)

        # Добавляем кнопку в футер и центрируем её
        footer_layout.addStretch()
        footer_layout.addWidget(self.add_notes_button)
        footer_layout.addStretch()

        # Добавляем футер в основной layout
        self.layout.addWidget(footer_widget)

        self.setLayout(self.layout)

    
    def add_notes_widget(self):
        ...
