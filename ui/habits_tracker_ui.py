from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QGridLayout, QScrollArea, QLineEdit, QInputDialog
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


class HabitsButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/habits.png")) 
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


class HabitsDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Habits Tracker")
        self.setFixedSize(900, 600)

        # Основной макет
        self.layout = QVBoxLayout()

        # Создаем QScrollArea для добавления скролла
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Разрешаем изменение размера содержимого

        # Виджет для содержимого QScrollArea
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)

        # Макет для квадратных виджетов внутри QScrollArea
        self.grid_layout = QGridLayout(self.scroll_content)
        self.grid_layout.setSpacing(10)  # Отступы между квадратами

        # Добавляем QScrollArea в основной макет
        self.layout.addWidget(self.scroll_area)

        # Создаем футер
        footer_layout = QHBoxLayout()
        footer_widget = QWidget()
        footer_widget.setLayout(footer_layout)

        # Кнопка "Добавить задачу"
        self.add_habits_button = QPushButton()
        self.add_habits_button.setFixedSize(100, 30)
        self.add_habits_button.setIcon(QIcon("resources/icons/add.png"))
        self.add_habits_button.setIconSize(QSize(30, 30))
        self.add_habits_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.add_habits_button.clicked.connect(self.add_square_widget)  # Подключаем сигнал

        # Добавляем кнопку в футер и центрируем её
        footer_layout.addStretch()
        footer_layout.addWidget(self.add_habits_button)
        footer_layout.addStretch()

        # Добавляем футер в основной layout
        self.layout.addWidget(footer_widget)

        self.setLayout(self.layout)

        # Счетчик для квадратных виджетов
        self.square_counter = 0


    def add_square_widget(self):
        """Добавляет квадратный виджет в макет."""
        # Создаем квадратный виджет
        square_widget = QFrame()
        square_widget.setFixedSize(250, 250)  # Размер квадрата
        square_widget.setStyleSheet("background-color: rgba(255, 255, 255, 0); border-radius: 15px; border: 1px solid white; color: white;")

        # Внутренний макет для квадрата
        square_layout = QVBoxLayout()
        square_widget.setLayout(square_layout)

        # Поле ввода названия привычки
        habit_label = QLineEdit()
        habit_label.setPlaceholderText("Название привычки")
        habit_label.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); border-radius: 5px; color: white; padding: 5px;")
        habit_label.setReadOnly(True)  # Поле изначально недоступно для редактирования
        square_layout.addWidget(habit_label)

        # Кнопки "Редактировать", "Сохранить" и "Удалить"
        buttons_layout = QHBoxLayout()
        square_layout.addLayout(buttons_layout)

        # Кнопка "Редактировать"
        edit_habit = QPushButton("✏️")
        edit_habit.setFixedSize(QSize(30, 30))
        edit_habit.clicked.connect(lambda: self.edit_habit(habit_label, save_habit))
        buttons_layout.addWidget(edit_habit)

        # Кнопка "Сохранить"
        save_habit = QPushButton("✔️")
        save_habit.setFixedSize(QSize(30, 30))
        save_habit.clicked.connect(lambda: self.save_habit(habit_label))
        save_habit.setEnabled(False)  # Кнопка "Сохранить" изначально неактивна
        buttons_layout.addWidget(save_habit)

        # Кнопка "Удалить"
        delete_habit = QPushButton("❌")
        delete_habit.setFixedSize(QSize(30, 30))
        delete_habit.clicked.connect(lambda: self.delete_habit(square_widget))
        buttons_layout.addWidget(delete_habit)

        # Вычисляем позицию для нового квадрата
        row = self.square_counter // 3
        col = self.square_counter % 3

        # Добавляем квадрат в макет
        self.grid_layout.addWidget(square_widget, row, col)

        # Увеличиваем счетчик
        self.square_counter += 1

        # Если квадратов больше 3 в строке, добавляем новую строку
        if self.square_counter % 3 == 0:
            self.grid_layout.setRowStretch(row, 1)  # Растягиваем новую строку

    def edit_habit(self, habit_label, save_button):
        """Метод для редактирования задачи."""
        habit_label.setReadOnly(False)  # Делаем поле доступным для редактирования
        habit_label.setFocus()  # Устанавливаем фокус на поле ввода
        save_button.setEnabled(True)  # Активируем кнопку "Сохранить"

    def save_habit(self, habit_label):
        """Метод для сохранения данных карточки."""
        habit_label.setReadOnly(True)  # Делаем поле недоступным для редактирования

    def delete_habit(self, square_widget):
        """Метод для удаления задачи."""
        self.grid_layout.removeWidget(square_widget)
        square_widget.deleteLater()
        self.square_counter -= 1
