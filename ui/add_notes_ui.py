from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QWidget, QTextEdit, QScrollArea, QGridLayout, QMessageBox, QLineEdit
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon

from datetime import datetime

from database.db_notes_manager import create_notes_db, add_note


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
        self.setWindowTitle("BED - Add Note")
        self.setFixedSize(900, 600)

        # Основной макет
        self.layout = QVBoxLayout(self)

        # Контейнер для заметок (текстовых редакторов и заголовков)
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

        # Футер с кнопкой "Сохранить заметку"
        footer_widget = QWidget()
        footer_layout = QGridLayout(footer_widget)
        footer_layout.setContentsMargins(0, 10, 0, 10)

        # Кнопка "Сохранить заметку"
        self.save_notes_button = QPushButton()
        self.save_notes_button.setFixedSize(100, 30)
        self.save_notes_button.setIcon(QIcon("resources/icons/save.png"))
        self.save_notes_button.setIconSize(QSize(30, 30))
        self.save_notes_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.save_notes_button.clicked.connect(self.save_note)

        # Добавляем кнопку "Сохранить заметку" в центр футера
        footer_layout.addWidget(self.save_notes_button, 0, 1, alignment=Qt.AlignCenter)

        # Добавляем футер в основной макет
        self.layout.addWidget(footer_widget)

        # Переменные для хранения текущего текстового редактора и поля ввода названия
        self.current_title_edit = None
        self.current_text_edit = None

        # Создаем таблицу при инициализации
        create_notes_db()

        # Добавляем текстовый редактор и поле ввода названия при инициализации
        self.add_notes_widget()

    def add_notes_widget(self):
        # Проверяем, существует ли уже текстовый редактор и поле ввода названия
        if self.current_text_edit is not None or self.current_title_edit is not None:
            return

        # Создаем поле ввода названия заметки
        self.current_title_edit = QLineEdit()
        self.current_title_edit.setPlaceholderText("Title (symbols number <= 50)")
        self.current_title_edit.setMaxLength(50)
        self.current_title_edit.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 15px;
                border: 1px solid white;
                border-radius: 15px;
            }
        """)

        # Создаем текстовый редактор
        self.current_text_edit = QTextEdit()
        self.current_text_edit.setPlaceholderText("Text of your note is here...")
        self.current_text_edit.setMinimumHeight(200)

        # Добавляем поле ввода названия и текстовый редактор в контейнер заметок
        self.notes_container.addWidget(self.current_title_edit)
        self.notes_container.addWidget(self.current_text_edit)

        # Подключаем сигнал закрытия редактора (если нужно)
        self.current_text_edit.destroyed.connect(self.on_text_edit_closed)
        self.current_title_edit.destroyed.connect(self.on_title_edit_closed)


    def save_note(self):
        if self.current_text_edit is not None and self.current_title_edit is not None:
            title = self.current_title_edit.text().strip()

            if title == "":
                title = datetime.now().strftime("Note without a name: %d.%m.%Y")
            content = self.current_text_edit.toPlainText()
            add_note(title, content)
            self.close()


    def on_text_edit_closed(self):
        # Очищаем ссылку на текстовый редактор при его закрытии
        self.current_text_edit = None


    def on_title_edit_closed(self):
        # Очищаем ссылку на поле ввода названия при его закрытии
        self.current_title_edit = None
