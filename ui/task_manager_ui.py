from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QDateEdit,
    QPushButton, QFormLayout, QTextEdit, QWidget,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QCheckBox,
)
from PySide6.QtCore import QTimer, QTime, QDate, QSize, Qt
from PySide6.QtGui import QIcon, QFont


class TaskManagerUI(QWidget):
    def __init__(self):
        super().__init__()

        # Основной макет
        self.layout = QVBoxLayout(self)

        # Живой таймер (показывает текущее время)
        self.timer_label = QLabel("00:00:00", self)
        self.timer_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: white;
                background-color: rgba(0, 0, 0, 0.5);
                border-radius: 10px;
            }
        """)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.timer_label)

        # Список задач
        self.task_list = QListWidget()
        self.task_list.setStyleSheet("""
            QListWidget {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
            }
        """)
        self.layout.addWidget(self.task_list)

        # Текст, который отображается, если задач нет
        self.empty_item = QListWidgetItem("\nУспейте выполнить все задачи!")
        self.empty_item.setTextAlignment(Qt.AlignCenter)
        self.empty_item.setForeground(Qt.gray)
        self.task_list.addItem(self.empty_item)  # Добавляем текст в список задач

        # Горизонтальный макет для центрирования кнопки
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Добавляем растягивающийся элемент слева

        # Кнопка "Добавить задачу"
        self.add_task_button = QPushButton()
        self.add_task_button.setFixedSize(100, 30)
        self.add_task_button.setIcon(QIcon("resources/icons/add.png"))
        self.add_task_button.setIconSize(QSize(30, 30))
        self.add_task_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.add_task_button.clicked.connect(self.show_add_task_dialog)  # Подключаем сигнал
        button_layout.addWidget(self.add_task_button)

        button_layout.addStretch()  # Добавляем растягивающийся элемент справа

        # Добавляем горизонтальный макет с кнопкой в основной макет
        self.layout.addLayout(button_layout)

        # Таймер для обновления времени
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Обновление каждую секунду

        # Подключаем сигнал изменения списка задач
        self.task_list.itemChanged.connect(self.update_empty_label)


    def show_add_task_dialog(self):
        """Показывает диалоговое окно для добавления задачи."""
        dialog = AddTaskDialog(self)
        if dialog.exec() == QDialog.Accepted:
            task_data = dialog.get_task_data()
            self.add_task_item(task_data["name"], task_data["description"])


    def update_time(self):
        """Обновляет время на таймере."""
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.timer_label.setText(current_time)


    def update_empty_label(self):
        """Скрывает или показывает текст, если задач нет."""
        if self.task_list.count() == 1 and self.task_list.item(0) == self.empty_item:
            self.task_list.takeItem(0)
        elif self.task_list.count() == 0:
            self.task_list.addItem(self.empty_item)


    def add_task_item(self, task_text, task_description):
        """Добавляет задачу в список."""
        item = QListWidgetItem()
        self.task_list.addItem(item)

        # Создаём виджет для задачи
        task_widget = QWidget()
        task_layout = QHBoxLayout()

        # Чекбокс для отметки выполненной задачи
        checkbox = QCheckBox()
        checkbox.setFixedSize(QSize(20, 20))
        task_layout.addWidget(checkbox)

        # Текст задачи
        task_label = QLineEdit(task_text)
        task_label.setReadOnly(True)
        task_layout.addWidget(task_label)

        # Кнопка "Редактировать"
        edit_button = QPushButton("✏️")
        edit_button.setFixedSize(QSize(30, 30))
        task_layout.addWidget(edit_button)

        # Устанавливаем layout для виджета задачи
        task_widget.setLayout(task_layout)
        item.setSizeHint(task_widget.sizeHint())
        self.task_list.setItemWidget(item, task_widget)

        # Возвращаем элементы для дальнейшей работы
        return item, checkbox, task_label, edit_button


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
