from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QTextEdit, QLineEdit
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QIcon

from datetime import datetime

from database.db_notes_manager import create_notes_db, add_note, get_note, update_note


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
    # Создаем сигнал для обновления списка заметок
    note_saved = Signal()

    def __init__(self, parent=None, note_id=None):
        super().__init__(parent)
        self.note_id = note_id
        self.setWindowTitle("BED - Add Note" if not note_id else "BED - Edit Note")
        self.setFixedSize(900, 600)

        # Основной макет
        self.layout = QVBoxLayout(self)

        # Поле ввода названия заметки
        self.current_title_edit = QLineEdit()
        self.current_title_edit.setPlaceholderText("Title (does not change)")
        self.current_title_edit.setMaxLength(50)
        self.current_title_edit.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 20px;
                border: 1px solid white;
                border-radius: 15px;
            }
            QLineEdit:read-only {
                background-color: grey;
                border: 1px solid grey;
                color: #555;
            }
        """)
        self.layout.addWidget(self.current_title_edit)

        # Текстовый редактор для содержимого заметки
        self.current_text_edit = QTextEdit()
        self.current_text_edit.setPlaceholderText("Text of your note is here...")
        self.current_text_edit.setMinimumHeight(200)
        self.current_text_edit.setStyleSheet("""
            QTextEdit {
                font-size: 15px;
            }
        """)
        self.layout.addWidget(self.current_text_edit)

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
        self.layout.addWidget(self.save_notes_button, alignment=Qt.AlignCenter)

        # Создаем таблицу при инициализации
        create_notes_db()

        # Если передан note_id, загружаем данные заметки
        if self.note_id:
            self.load_note()


    def load_note(self):
        """Загружает данные существующей заметки для редактирования."""
        note = get_note(self.note_id)
        if note:
            self.current_title_edit.setText(note["title"])
            self.current_text_edit.setPlainText(note["content"])
            self.current_title_edit.setReadOnly(True)


    def save_note(self):
        """Сохраняет новую заметку или обновляет существующую."""
        title = self.current_title_edit.text().strip()
        content = self.current_text_edit.toPlainText()

        if not title:
            title = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.note_id:
            update_note(self.note_id, title, content)
        else:
            add_note(title, content)

        self.current_title_edit.setReadOnly(True)
        self.note_saved.emit()
        self.close()
