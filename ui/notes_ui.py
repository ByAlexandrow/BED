from PySide6.QtWidgets import QDialog, QVBoxLayout, QScrollArea, QWidget, QGridLayout, QPushButton, QLabel, QFrame, QHBoxLayout
from PySide6.QtGui import QIcon, Qt
from PySide6.QtCore import QSize

from ui.add_notes_ui import AddNotesDialogUI

from database.db_notes_manager import get_all_notes, delete_note


class NoteFrame(QFrame):
    def __init__(self, note_id, parent=None):
        super().__init__(parent)
        self.note_id = note_id


    def mouseDoubleClickEvent(self, event):
        """Обработчик двойного клика."""
        edit_dialog = AddNotesDialogUI(self.parent(), self.note_id)
        edit_dialog.exec_()
        self.parent().load_notes()


class AllNotesDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Notes")
        self.setFixedSize(900, 600)

        # Основной макет
        self.layout = QVBoxLayout(self)

        # Контейнер для заметок
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

        # Футер с кнопкой "Добавить заметку"
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
        self.add_notes_button.clicked.connect(self.add_notes)

        # Добавляем кнопку "Добавить заметку" в центр футера
        footer_layout.addWidget(self.add_notes_button, 0, 1, alignment=Qt.AlignCenter)

        # Добавляем футер в основной макет
        self.layout.addWidget(footer_widget)

        # Загружаем существующие заметки
        self.load_notes()


    def add_notes(self):
        """Открывает диалог для добавления новой заметки."""
        add_dialog = AddNotesDialogUI(self)
        add_dialog.note_saved.connect(self.load_notes)
        add_dialog.exec_()


    def delete_note(self, note_id):
        """Удаляет заметку и обновляет список."""
        delete_note(note_id)
        self.load_notes()


    def load_notes(self):
        """Загружает и отображает все заметки."""
        for i in reversed(range(self.notes_container.count())):
            self.notes_container.itemAt(i).widget().setParent(None)

        notes = get_all_notes()

        for note in notes:
            note_frame = NoteFrame(note["id"])
            note_frame.setFrameShape(QFrame.Panel)
            note_frame.setFixedSize(850, 50)

            note_layout = QHBoxLayout(note_frame)
            note_layout.setSpacing(5)
            note_layout.setContentsMargins(10, 5, 10, 5)

            title_label = QLabel(note["title"])
            title_label.setStyleSheet("""
                QLabel {
                    font-size: 15px;
                    font-weight: normal;
                    color: white;
                }
            """)
            note_layout.addWidget(title_label, stretch=1)

            # Кнопка удаления
            delete_button = QPushButton("❌")
            delete_button.setFixedSize(30, 30)
            delete_button.clicked.connect(lambda _, note_id=note["id"]: self.delete_note(note_id))
            note_layout.addWidget(delete_button)

            # Добавляем рамку с заметкой в контейнер
            self.notes_container.addWidget(note_frame)
