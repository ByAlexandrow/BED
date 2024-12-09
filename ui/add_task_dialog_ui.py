from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel, QHBoxLayout, QButtonGroup
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont


class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("BED - New Task")
        self.setFixedSize(325, 450)

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

        # Поле установления уровня сложности
        task_level_layout = QVBoxLayout()
        self.task_level_label = QLabel("Срочность")
        self.task_level_label.setFont(label_font)
        task_level_layout.addWidget(self.task_level_label)

        # Горизонтальный макет для иконок
        icons_layout = QHBoxLayout()

        # Группа кнопок для уровня сложности
        self.task_level_group = QButtonGroup(self)
        self.task_level_group.setExclusive(True)  # Только одна иконка может быть выбрана

        # Иконка "Срочно" (красная)
        self.urgent_button = QPushButton()
        self.urgent_button.setIcon(QIcon("resources/icons/red_clock.png"))
        self.urgent_button.setIconSize(QSize(30, 30))
        self.urgent_button.setFixedSize(40, 40)
        self.urgent_button.clicked.connect(lambda: self.set_level("Срочно"))
        self.task_level_group.addButton(self.urgent_button)
        icons_layout.addWidget(self.urgent_button)

        # Иконка "Средне" (оранжевая)
        self.medium_button = QPushButton()
        self.medium_button.setIcon(QIcon("resources/icons/orange_clock.png"))
        self.medium_button.setIconSize(QSize(30, 30))
        self.medium_button.setFixedSize(40, 40)
        self.medium_button.clicked.connect(lambda: self.set_level("Средне"))
        self.task_level_group.addButton(self.medium_button)
        icons_layout.addWidget(self.medium_button)

        # Иконка "Не срочно" (зеленая)
        self.not_urgent_button = QPushButton()
        self.not_urgent_button.setIcon(QIcon("resources/icons/green_clock.png"))
        self.not_urgent_button.setIconSize(QSize(30, 30))
        self.not_urgent_button.setFixedSize(40, 40)
        self.not_urgent_button.clicked.connect(lambda: self.set_level("Не срочно"))
        self.task_level_group.addButton(self.not_urgent_button)
        icons_layout.addWidget(self.not_urgent_button)

        # Добавляем макет с иконками в основной макет
        task_level_layout.addLayout(icons_layout)
        layout.addLayout(task_level_layout)

        # Добавляем пустое пространство между иконками и кнопкой "ОК"
        layout.addStretch(1)  # Добавляем растягивающийся элемент

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

        # Инициализация выбранного уровня
        self.selected_level = None

    def set_level(self, level):
        """Устанавливает выбранный уровень сложности."""
        self.selected_level = level

    def get_task_data(self):
        """Возвращает данные задачи."""
        return {
            "name": self.task_name_edit.text(),
            "description": self.task_description_edit.toPlainText(),
            "level": self.selected_level
        }
