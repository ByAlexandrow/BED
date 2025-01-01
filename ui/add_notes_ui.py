from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QTextEdit, QLineEdit, QHBoxLayout, QToolButton, QComboBox
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QIcon, QTextCharFormat

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
                font-size: 15px;
                border: 1px solid white;
                border-radius: 15px;
            }
            QLineEdit:read-only {
                background-color: rgba(0, 0, 0, 0.1);
                border: 1px solid white;
                color: white;
            }
        """)
        self.layout.addWidget(self.current_title_edit)

        # Панель инструментов для форматирования текста
        self.toolbar_layout = QHBoxLayout()

        # Кнопка для жирного текста
        self.bold_button = QToolButton()
        self.bold_button.setText("B")
        self.bold_button.setCheckable(True)
        self.bold_button.clicked.connect(self.toggle_bold)
        self.bold_button.setMinimumSize(30, 30)
        self.bold_button.setStyleSheet("""
            QToolButton {
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 5px 10px;
                font-size: 17px;
            }
            QToolButton:checked {
                background-color: white;
                color: black;
                border: 1px solid black;
            }
            QToolButton:hover {
                background-color: grey;
            }
        """)
        self.toolbar_layout.addWidget(self.bold_button)

        # Кнопка для курсива
        self.italic_button = QToolButton()
        self.italic_button.setText("I")
        self.italic_button.setCheckable(True)
        self.italic_button.clicked.connect(self.toggle_italic)
        self.italic_button.setMinimumSize(30, 30)
        self.italic_button.setStyleSheet("""
            QToolButton {
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 5px 10px;
                font-size: 17px;
            }
            QToolButton:checked {
                background-color: white;
                color: black;
                border: 1px solid black;
            }
            QToolButton:hover {
                background-color: grey;
            }
        """)
        self.toolbar_layout.addWidget(self.italic_button)

        # Кнопка для подчеркивания
        self.underline_button = QToolButton()
        self.underline_button.setText("U")
        self.underline_button.setCheckable(True)
        self.underline_button.clicked.connect(self.toggle_underline)
        self.underline_button.setMinimumSize(30, 30)
        self.underline_button.setStyleSheet("""
            QToolButton {
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 5px 10px;
                font-size: 17px;
            }
            QToolButton:checked {
                background-color: white;
                color: black;
                border: 1px solid black;
            }
            QToolButton:hover {
                background-color: grey;
            }
        """)
        self.toolbar_layout.addWidget(self.underline_button)

        # Выбор шрифта
        self.font_combo = QComboBox()
        self.font_combo.addItems(["Arial", "Times New Roman", "Courier New", "Verdana", "Georgia"])
        self.font_combo.currentTextChanged.connect(self.change_font)
        self.font_combo.setFixedSize(200, 30)
        self.font_combo.setStyleSheet("""
            QComboBox {
                background-color: rgba(0, 0, 0, 0.1);
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 5px;
                font-size: 15px;
            }
            QComboBox:hover {
                border: 1px solid white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border: none;
                padding: 8px;
            }
            QComboBox::down-arrow {
                image: url("resources/icons/arrow_down_btn.png");
                width: 17px;
                height: 17px;
            }
        """)
        self.toolbar_layout.addWidget(self.font_combo)

        # Выбор размера шрифта
        self.font_size_combo = QComboBox()
        self.font_size_combo.addItems(["10", "12", "14", "16", "18", "20", "24", "28", "32"])
        self.font_size_combo.currentTextChanged.connect(self.change_font_size)
        # self.font_size_combo.setFixedSize(200, 30)
        self.font_size_combo.setFixedHeight(30)
        self.font_size_combo.setStyleSheet("""
            QComboBox {
                background-color: rgba(0, 0, 0, 0.1);
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 5px;
                font-size: 15px;
            }
            QComboBox:hover {
                border: 1px solid white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border: none;
                padding: 8px;
            }
            QComboBox::down-arrow {
                image: url("resources/icons/arrow_down_btn.png");
                width: 17px;
                height: 17px;
            }
        """)
        self.toolbar_layout.addWidget(self.font_size_combo)

        self.layout.addLayout(self.toolbar_layout)

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


    def toggle_bold(self):
        """Переключает жирный шрифт."""
        cursor = self.current_text_edit.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontWeight(75 if not self.bold_button.isChecked() else 50)
        cursor.mergeCharFormat(fmt)
        self.current_text_edit.mergeCurrentCharFormat(fmt)


    def toggle_italic(self):
        """Переключает курсив."""
        cursor = self.current_text_edit.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontItalic(not self.italic_button.isChecked())
        cursor.mergeCharFormat(fmt)
        self.current_text_edit.mergeCurrentCharFormat(fmt)


    def toggle_underline(self):
        """Переключает подчеркивание."""
        cursor = self.current_text_edit.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontUnderline(not self.underline_button.isChecked())
        cursor.mergeCharFormat(fmt)
        self.current_text_edit.mergeCurrentCharFormat(fmt)


    def change_font(self):
        """Изменяет шрифт."""
        font = self.font_combo.currentText()
        cursor = self.current_text_edit.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontFamily(font)
        cursor.mergeCharFormat(fmt)
        self.current_text_edit.mergeCurrentCharFormat(fmt)


    def change_font_size(self):
        """Изменяет размер шрифта."""
        size = int(self.font_size_combo.currentText())
        cursor = self.current_text_edit.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontPointSize(size)
        cursor.mergeCharFormat(fmt)
        self.current_text_edit.mergeCurrentCharFormat(fmt)


    def load_note(self):
        """Загружает данные существующей заметки для редактирования."""
        note = get_note(self.note_id)
        if note:
            self.current_title_edit.setText(note["title"])
            self.current_text_edit.setHtml(note["content"])
            self.current_title_edit.setReadOnly(True)


    def save_note(self):
        """Сохраняет новую заметку или обновляет существующую."""
        title = self.current_title_edit.text().strip()
        content = self.current_text_edit.toHtml()

        if not title:
            title = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.note_id:
            update_note(self.note_id, title, content)
        else:
            add_note(title, content)

        self.current_title_edit.setReadOnly(True)
        self.note_saved.emit()
        self.close()
