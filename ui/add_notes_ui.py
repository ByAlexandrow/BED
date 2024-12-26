from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QWidget, QTextEdit, QScrollArea, QGridLayout
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon

from ui.all_notes_ui import AllNotesDialogUI


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


class AddNotesDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Add Notes")
        self.setFixedSize(900, 600)

        # Основной макет
        self.layout = QVBoxLayout(self)

        # Контейнер для заметок (текстовых редакторов)
        self.notes_container = QVBoxLayout()
        self.notes_container.setSpacing(10)

        # Область с прокруткой для заметок
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_widget.setLayout(self.notes_container)
        scroll_area.setWidget(scroll_widget)

        # Добавляем область с прокруткой в основной макет
        self.layout.addWidget(scroll_area)

        # Футер с кнопкой "Добавить заметку" и "Файлы"
        footer_widget = QWidget()
        footer_layout = QGridLayout(footer_widget)
        footer_layout.setContentsMargins(0, 10, 0, 10)

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
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.add_notes_button.clicked.connect(self.add_notes_widget)

        # Кнопка "Файлы"
        self.all_notes_button = QPushButton()
        self.all_notes_button.setFixedSize(100, 30)
        self.all_notes_button.setIcon(QIcon("resources/icons/files.png"))
        self.all_notes_button.setIconSize(QSize(30, 30))
        self.all_notes_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.all_notes_button.clicked.connect(self.all_notes)

        # Добавляем кнопку "Добавить заметку" в центр футера
        footer_layout.addWidget(self.add_notes_button, 0, 1, alignment=Qt.AlignCenter)

        # Добавляем кнопку "Файлы" в правый нижний угол футера
        footer_layout.addWidget(self.all_notes_button, 0, 1, alignment=Qt.AlignRight | Qt.AlignBottom)

        # Добавляем футер в основной макет
        self.layout.addWidget(footer_widget)

        # Переменная для хранения текущего текстового редактора
        self.current_text_edit = None

    
    def add_notes_widget(self):
        # Проверяем, существует ли уже текстовый редактор
        if self.current_text_edit is not None:
            return

        # Создаем текстовый редактор
        self.current_text_edit = QTextEdit()
        self.current_text_edit.setPlaceholderText("Text of your note is here...")
        self.current_text_edit.setMinimumHeight(200)

        # Добавляем текстовый редактор в контейнер заметок
        self.notes_container.addWidget(self.current_text_edit)

        # Подключаем сигнал закрытия редактора (если нужно)
        self.current_text_edit.destroyed.connect(self.on_text_edit_closed)


    def on_text_edit_closed(self):
        # Очищаем ссылку на текстовый редактор при его закрытии
        self.current_text_edit = None
    

    def all_notes(self):
        all_notes_dialog = AllNotesDialogUI(self)
        all_notes_dialog.show()
