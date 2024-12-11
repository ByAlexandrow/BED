from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, QLabel, QCheckBox, QLineEdit
)
from PySide6.QtCore import QTimer, QTime, QSize, Qt
from PySide6.QtGui import QIcon

from database.db_manager import (
    create_task_db, add_task_to_task_db, load_tasks_from_task_db,
    update_task_in_task_db, delete_task_from_task_db, mark_task_completed
)

from ui.add_task_dialog_ui import AddTaskDialog


class TaskManagerUI(QWidget):
    def __init__(self):
        super().__init__()

        # Создаём базу данных, если её нет
        create_task_db()

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
        self.empty_item = QListWidgetItem("Добавьте задачи!")
        self.empty_item.setTextAlignment(Qt.AlignCenter)
        self.empty_item.setForeground(Qt.gray)
        self.task_list.addItem(self.empty_item)

        # Загружаем задачи из базы данных
        self.load_tasks()

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
        if dialog.exec() == AddTaskDialog.Accepted:
            task_data = dialog.get_task_data()
            self.add_task_item(task_data["name"], task_data["description"])
            add_task_to_task_db(task_data["name"], task_data["description"])  # Добавляем задачу в базу данных


    def update_time(self):
        """Обновляет время на таймере."""
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.timer_label.setText(current_time)


    def update_empty_label(self):
        """Скрывает или показывает текст, если задач нет."""
        if self.task_list.count() == 1 and self.task_list.item(0) == self.empty_item:
            self.empty_item.setText("\nДобавьте задачи!")  # Текст, если задач нет
        elif self.task_list.count() == 0:
            self.task_list.addItem(self.empty_item)
            self.empty_item.setText("\nДобавьте задачи!")  # Текст, если задач нет
        else:
            self.empty_item.setText("\nУспейте выполнить все задачи!")  # Текст, если задачи есть


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
        checkbox.stateChanged.connect(lambda state: self.mark_task_completed(task_text, state))
        task_layout.addWidget(checkbox)

        # Текст задачи
        task_label = QLineEdit(task_text)
        task_label.setReadOnly(True)
        task_layout.addWidget(task_label)

        # Кнопка "Редактировать"
        edit_button = QPushButton("✏️")
        edit_button.setFixedSize(QSize(30, 30))
        edit_button.clicked.connect(lambda: self.edit_task(task_label, task_description))
        task_layout.addWidget(edit_button)

        # Кнопка "Удалить"
        delete_button = QPushButton("❌")
        delete_button.setFixedSize(QSize(30, 30))
        delete_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 0, 0, 0.1);
                border-radius: 15px;
                border: 1px solid red;
            }
            QPushButton:hover {
                background-color: rgba(255, 0, 0, 0.2);
            }
        """)
        delete_button.clicked.connect(lambda: self.delete_task(task_label.text(), item))
        task_layout.addWidget(delete_button)

        # Устанавливаем layout для виджета задачи
        task_widget.setLayout(task_layout)
        item.setSizeHint(task_widget.sizeHint())
        self.task_list.setItemWidget(item, task_widget)


    def edit_task(self, task_label, task_description):
        """Открывает диалоговое окно для редактирования задачи."""
        dialog = AddTaskDialog(self)
        dialog.task_name_edit.setText(task_label.text())
        dialog.task_description_edit.setText(task_description)

        if dialog.exec() == AddTaskDialog.Accepted:
            task_data = dialog.get_task_data()
            old_name = task_label.text()
            new_name = task_data["name"]
            new_description = task_data["description"]
            task_label.setText(new_name)
            update_task_in_task_db(old_name, new_name, new_description)  # Обновляем задачу в базе данных


    def delete_task(self, task_name, item):
        """Удаляет задачу."""
        # Удаляем задачу из интерфейса
        row = self.task_list.row(item)
        self.task_list.takeItem(row)

        # Удаляем задачу из базы данных
        delete_task_from_task_db(task_name)

        # Обновляем интерфейс, если задач не осталось
        self.update_empty_label()


    def mark_task_completed(self, task_name, completed):
        """Отмечает задачу как выполненную или невыполненную."""
        mark_task_completed(task_name, completed)


    def load_tasks(self):
        """Загружает задачи из базы данных."""
        tasks = load_tasks_from_task_db()
        for name, description, completed in tasks:
            self.add_task_item(name, description)
            # Отмечаем задачу как выполненную, если completed == 1
            if completed:
                item = self.task_list.item(self.task_list.count() - 1)
                widget = self.task_list.itemWidget(item)
                checkbox = widget.layout().itemAt(0).widget()
                checkbox.setChecked(True)

        # Обновляем текст в зависимости от наличия задач
        self.update_empty_label()