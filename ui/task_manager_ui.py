from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QHBoxLayout,
    QLabel, QTextEdit, QLineEdit
)
from PySide6.QtCore import QTimer, QTime, QSize, Qt
from PySide6.QtGui import QIcon

from database.db_tasks_manager import (
    create_tasks_db, add_tasks_to_tasks_db,
    load_tasks_from_tasks_db, update_tasks_in_tasks_db,
    delete_tasks_from_tasks_db, is_name_unique, get_task_id_by_name
)

from ui.add_task_dialog_ui import AddTaskDialog


class TaskManagerUI(QWidget):
    def __init__(self):
        super().__init__()

        # Создаём базу данных, если её нет
        create_tasks_db()

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
        self.timer.start(1000)

        # Подключаем сигнал изменения списка задач
        self.task_list.itemChanged.connect(self.update_empty_label)


    def show_add_task_dialog(self):
        """Показывает диалоговое окно для добавления задачи."""
        dialog = AddTaskDialog(self)
        if dialog.exec() == AddTaskDialog.Accepted:
            task_data = dialog.get_task_data()
            self.add_task_item(task_data["name"], task_data["description"], task_data["level"])
            add_tasks_to_tasks_db(task_data["name"], task_data["description"], task_data["level"])


    def update_time(self):
        """Обновляет время на таймере."""
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.timer_label.setText(current_time)


    def update_empty_label(self):
        """Скрывает или показывает текст, если задач нет."""
        if self.task_list.count() == 1 and self.task_list.item(0) == self.empty_item:
            self.empty_item.setText("\nДобавьте задачи!")
        elif self.task_list.count() == 0:
            self.task_list.addItem(self.empty_item)
            self.empty_item.setText("\nДобавьте задачи!")
        else:
            self.empty_item.setText("\nУспейте выполнить все задачи!")


    def add_task_item(self, task_text, task_description, task_level):
        """Добавляет задачу в список."""
        item = QListWidgetItem()
        self.task_list.addItem(item)

        # Создаём виджет для задачи
        task_widget = QWidget()
        task_layout = QHBoxLayout()

        # Срочность задачи
        level_icon = QLabel()
        level_icon.setPixmap(self.get_level_icon(task_level))
        task_layout.addWidget(level_icon)

        # Текст задачи
        task_label = QLineEdit(task_text)
        task_label.setReadOnly(True)
        task_label.setFixedHeight(30)
        task_layout.addWidget(task_label)

        # Поле для описания задачи
        task_description_edit = QTextEdit(task_description)
        task_description_edit.setVisible(False)
        task_layout.addWidget(task_description_edit)

        # Кнопка "Редактировать"
        edit_button = QPushButton("✏️")
        edit_button.setFixedSize(QSize(30, 30))
        edit_button.clicked.connect(lambda: self.edit_task(task_label, task_description_edit, level_icon))
        task_layout.addWidget(edit_button)

        # Кнопка "Удалить"
        delete_button = QPushButton("❌")
        delete_button.setFixedSize(QSize(30, 30))
        delete_button.clicked.connect(lambda: self.delete_task(task_label.text(), item))
        task_layout.addWidget(delete_button)

        # Устанавливаем layout для виджета задачи
        task_widget.setLayout(task_layout)
        item.setSizeHint(task_widget.sizeHint())
        self.task_list.setItemWidget(item, task_widget)


    def edit_task(self, task_label, task_description_edit, level_icon):
        """Открывает диалоговое окно для редактирования задачи."""
        dialog = AddTaskDialog(self, original_task_name=task_label.text())
        dialog.task_name_edit.setText(task_label.text())
        dialog.task_description_edit.setText(task_description_edit.toPlainText())  # Устанавливаем текущее описание

        if dialog.exec() == AddTaskDialog.Accepted:
            task_data = dialog.get_task_data()
            old_name = task_label.text()
            new_name = task_data["name"]
            new_description = task_data["description"]
            new_level = task_data["level"]

            # Получаем task_id текущей задачи
            task_id = get_task_id_by_name(old_name)

            # Проверяем, уникально ли новое имя (исключая текущую задачу)
            if not is_name_unique(new_name, task_id):
                self.show_error("Такое имя уже существует")
                return

            # Обновляем задачу в базе данных
            update_tasks_in_tasks_db(old_name, new_name, task_description_edit.toPlainText(), new_description, new_level)

            # Обновляем интерфейс сразу
            task_label.setText(new_name)
            task_description_edit.setText(new_description)
            level_icon.setPixmap(self.get_level_icon(new_level))


    def delete_task(self, task_name, item):
        """Удаляет задачу."""
        # Удаляем задачу из интерфейса
        row = self.task_list.row(item)
        self.task_list.takeItem(row)

        # Удаляем задачу из базы данных
        delete_tasks_from_tasks_db(task_name)

        # Обновляем интерфейс, если задач не осталось
        self.update_empty_label()


    def load_tasks(self):
        """Загружает задачи из базы данных."""
        tasks = load_tasks_from_tasks_db()
        for name, description, level in tasks:
            self.add_task_item(name, description, level)

        # Обновляем текст в зависимости от наличия задач
        self.update_empty_label()
    

    def get_level_icon(self, level):
        """Возвращает иконку в зависимости от уровня срочности."""
        if level == "Срочно":
            return QIcon("resources/icons/red_rush.png").pixmap(QSize(30, 30))
        elif level == "Средне":
            return QIcon("resources/icons/orange_rush.png").pixmap(QSize(30, 30))
        else:
            return QIcon("resources/icons/green_rush.png").pixmap(QSize(30, 30))
