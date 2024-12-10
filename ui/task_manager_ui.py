from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem,
    QPushButton, QCheckBox, QLineEdit
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer, QTime, QSize, Qt


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
        self.empty_item = QListWidgetItem("\nУспейте выполнить все задачи до 22:00!")
        self.empty_item.setTextAlignment(Qt.AlignCenter)  # Выравниваем текст по центру
        self.empty_item.setForeground(Qt.gray)  # Устанавливаем цвет текста
        self.task_list.addItem(self.empty_item)  # Добавляем текст в список задач

        # Горизонтальный макет для центрирования кнопки
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Добавляем растягивающийся элемент слева

        # Кнопка "Добавить задачу" внутри блока
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


    def update_time(self):
        """Обновляет время на таймере."""
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.timer_label.setText(current_time)


    def update_empty_label(self):
        """Скрывает или показывает текст, если задач нет."""
        if self.task_list.count() == 1 and self.task_list.item(0) == self.empty_item:
            self.task_list.takeItem(0)  # Удаляем текст, если есть задачи
        elif self.task_list.count() == 0:
            self.task_list.addItem(self.empty_item)  # Показываем текст, если задач нет


    def add_task_item(self, task_text):
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

        # Кнопка "Удалить"
        delete_button = QPushButton("❌")
        delete_button.setFixedSize(QSize(30, 30))
        task_layout.addWidget(delete_button)

        # Устанавливаем layout для виджета задачи
        task_widget.setLayout(task_layout)
        item.setSizeHint(task_widget.sizeHint())
        self.task_list.setItemWidget(item, task_widget)

        # Возвращаем элементы для дальнейшей работы
        return item, checkbox, task_label, edit_button, delete_button
    