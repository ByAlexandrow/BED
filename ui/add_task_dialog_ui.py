from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QFont


class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("BED - New Task")
        self.setFixedSize(300, 400)

        # Основной макет
        layout = QVBoxLayout(self)

        # Стили для текста над полями ввода
        label_font = QFont("Arial", 12)

        # Поле для ввода имени задачи
        task_name_layout = QVBoxLayout()
        self.task_name_label = QLabel("Название")
        self.task_name_label.setFont(label_font)
        self.task_name_edit = QLineEdit(self)
        self.task_name_edit.setStyleSheet("""
            QLineEdit {
                background-color: rgba(0, 0, 0, 0.4);
                border: 1px solid #ccc;
                border-radius: 15px;
                color: white;
                padding: 5px;
            }
        """)
        task_name_layout.addWidget(self.task_name_label)
        task_name_layout.addWidget(self.task_name_edit)
        layout.addLayout(task_name_layout)

        # Поле для ввода описания задачи
        task_description_layout = QVBoxLayout()
        self.task_description_label = QLabel("Описание")
        self.task_description_label.setFont(label_font)
        self.task_description_edit = QTextEdit(self)
        self.task_description_edit.setStyleSheet("""
            QTextEdit {
                background-color: rgba(0, 0, 0, 0.4);
                border: 1px solid #ccc;
                border-radius: 15px;
                color: white;
                padding: 5px;
            }
        """)
        task_description_layout.addWidget(self.task_description_label)
        task_description_layout.addWidget(self.task_description_edit)
        layout.addLayout(task_description_layout)

        # Кнопка "ОК"
        button_box = QHBoxLayout()

        ok_button = QPushButton()
        ok_button.setFixedSize(90, 50)
        ok_button.setIcon(QIcon("resources/icons/ok.png"))
        ok_button.setIconSize(QSize(40, 40))
        ok_button.clicked.connect(self.accept)
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                border: 1px solid white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        button_box.addWidget(ok_button)

        layout.addLayout(button_box)

        # Стили для диалогового окна
        self.setStyleSheet("""
            QDialog {
                background-color: #2e2e2e;
            }
            QLabel {
                color: white;
            }
        """)


    def get_task_data(self):
        """Возвращает данные задачи."""
        return {
            "name": self.task_name_edit.text(),
            "description": self.task_description_edit.toPlainText(),
        }
