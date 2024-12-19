from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QSize


class AccountDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Account")
        self.setFixedSize(550, 650)

        # Основной вертикальный макет
        layout = QVBoxLayout()

        # Добавляем растягивающийся элемент сверху, чтобы поднять текст выше
        layout.addStretch(1.65)  # Увеличиваем вес растягивающегося элемента

        # Иконка
        self.security_icon = QLabel()
        self.security_icon.setPixmap(QPixmap("resources/icons/security.png").scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.security_icon.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.security_icon)

        # Отступ между иконкой и текстом
        layout.addSpacing(20)

        # Текст "Рекомендуем заполнить все поля и установить пароль"
        self.info_label = QLabel("Рекомендуем заполнить все поля и установить пароль\nЭто необходимо для безопасности ваших данных\nВы можете изменить их в любой момент\nПри входе в приложение потребуется ввести пароль, никнейм и код")
        self.info_label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 12)
        self.info_label.setFont(font)
        layout.addWidget(self.info_label)

        # Добавляем растягивающийся элемент между текстом и полями ввода
        layout.addStretch(2)

        # Горизонтальный макет для центрирования всех элементов
        center_layout = QHBoxLayout()

        # Вертикальный макет для пар "текст + поле"
        fields_layout = QVBoxLayout()
        fields_layout.setSpacing(20)  # Расстояние между элементами

        # Поле для ввода пароля
        password_layout = QVBoxLayout()
        self.password_label = QLabel("Пароль")
        self.password_label.setFont(font)
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Количество символов <= 20")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedSize(300, 35)
        self.password_input.setStyleSheet("""
            QLineEdit {
                background-color: rgba(0, 0, 0, 0.5);
                border: 1px solid white;
                border-radius: 10px;
            }
        """)
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)
        fields_layout.addLayout(password_layout)

        # Поле для ввода никнейма
        nickname_layout = QVBoxLayout()
        self.nickname_label = QLabel("Никнейм")
        self.nickname_label.setFont(font)
        self.nickname_label.setAlignment(Qt.AlignCenter)
        self.nickname_input = QLineEdit()
        self.nickname_input.setPlaceholderText("Количество символов <= 10")
        self.nickname_input.setFixedSize(300, 35)
        self.nickname_input.setStyleSheet("""
            QLineEdit {
                background-color: rgba(0, 0, 0, 0.5);
                border: 1px solid white;
                border-radius: 10px;
            }
        """)
        nickname_layout.addWidget(self.nickname_label)
        nickname_layout.addWidget(self.nickname_input)
        fields_layout.addLayout(nickname_layout)

        # Поле для ввода кода
        code_layout = QVBoxLayout()
        self.code_label = QLabel("Код")
        self.code_label.setFont(font)
        self.code_label.setAlignment(Qt.AlignCenter)
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Количество символов <= 5")
        self.code_input.setFixedSize(300, 35)
        self.code_input.setStyleSheet("""
            QLineEdit {
                background-color: rgba(0, 0, 0, 0.5);
                border: 1px solid white;
                border-radius: 10px;
            }
        """)
        code_layout.addWidget(self.code_label)
        code_layout.addWidget(self.code_input)
        fields_layout.addLayout(code_layout)

        # Добавляем вертикальный макет с полями в центр
        center_layout.addStretch()  # Растягивающийся элемент для центрирования
        center_layout.addLayout(fields_layout)
        center_layout.addStretch()  # Растягивающийся элемент для центрирования

        # Добавляем центрирующий макет в основной макет
        layout.addLayout(center_layout)

        # Добавляем растягивающийся элемент перед кнопками, чтобы опустить их ниже
        layout.addStretch(3)  # Увеличиваем вес растягивающегося элемента

        # Кнопки "Сохранить" и "Изменить"
        button_layout = QHBoxLayout()  # Горизонтальный макет для кнопок
        button_layout.addStretch()  # Растягивающийся элемент для центрирования

        self.save_button = QPushButton()
        self.save_button.setFixedSize(90, 50)
        self.save_button.setIcon(QIcon("resources/icons/save.png"))
        self.save_button.setIconSize(QSize(40, 40))
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.save_button.clicked.connect(self.save_data)

        self.change_button = QPushButton()
        self.change_button.setFixedSize(90, 50)
        self.change_button.setIcon(QIcon("resources/icons/edit.png"))
        self.change_button.setIconSize(QSize(40, 40))
        self.change_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.change_button.clicked.connect(self.change_data)

        button_layout.addWidget(self.change_button)
        button_layout.addWidget(self.save_button)
        button_layout.addStretch()  # Растягивающийся элемент для центрирования
        layout.addLayout(button_layout)

        # Добавляем растягивающийся элемент снизу, чтобы поднять кнопки выше
        layout.addStretch(1)

        self.setLayout(layout)

    def save_data(self):
        """
        Обработчик для кнопки "Сохранить".
        """
        password = self.password_input.text()
        nickname = self.nickname_input.text()
        code = self.code_input.text()
        print(f"Сохраненные данные: Пароль={password}, Никнейм={nickname}, Код={code}")

    def change_data(self):
        """
        Обработчик для кнопки "Изменить".
        """
        self.password_input.clear()
        self.nickname_input.clear()
        self.code_input.clear()
        print("Данные очищены для изменения.")
