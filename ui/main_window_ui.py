from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

from ui.topbar import TopBar
from ui.about_dialog_ui import AboutDialogUI
from ui.account_dialog_ui import AccountDialogUI
from ui.task_manager_ui import TaskManagerUI
from ui.ai_ui import AIButtonUI, AIDialogUI
from ui.habits_tracker_ui import HabitsButtonUI, HabitsDialogUI
from ui.notes_ui import NotesButtonUI, NotesDialogUI
from ui.achievements_ui import AchievementsButtonUI, AchievementsDialogUI
from ui.info_ui import InfoButtonUI, InfoDialogUI
from ui.settings import SettingsButtonUI, SettingsDialogUI
from ui.footer import Footer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('resources/favicon/main.png'))
        self.setWindowTitle("BED - Better Every Day")

        # Инициализируем интерфейс
        self.init_ui()

        # Устанавливаем стиль для главного окна
        self.setStyleSheet("""
            QMainWindow {
                background-image: url("resources/background/anonim.jpg");
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

    def init_ui(self):
        # Создаём TopBar
        self.top_bar = TopBar(self)
        self.top_bar.account_button.clicked.connect(self.show_account_dialog)
        self.top_bar.about_button.clicked.connect(self.show_about_dialog)

        # Создаём интерфейс TaskManagerUI
        self.task_manager_ui = TaskManagerUI()

        # Устанавливаем фиксированные размеры для TaskManagerUI
        self.task_manager_ui.setFixedWidth(300)

        # Создаём основной виджет с вертикальным компоновщиком
        main_layout_widget = QWidget()
        main_layout = QVBoxLayout(main_layout_widget)

        # Добавляем TopBar в верхнюю часть
        main_layout.addWidget(self.top_bar)

        # Создаём горизонтальный макет для TaskManagerUI и остального содержимого
        content_layout = QHBoxLayout()

        # Добавляем TaskManagerUI слева
        content_layout.addWidget(self.task_manager_ui)

        # Добавляем растягивающийся элемент, чтобы TaskManagerUI оставался слева
        content_layout.addStretch()

        # Добавляем горизонтальный макет в основной вертикальный макет
        main_layout.addLayout(content_layout)

        # Добавляем Footer в нижнюю часть
        self.footer = Footer()
        main_layout.addWidget(self.footer)

        # Устанавливаем основной виджет в качестве центрального виджета
        self.setCentralWidget(main_layout_widget)

        # Добавляем кнопку трекера AI
        self.ai_button = AIButtonUI(self)
        self.ai_button.clicked.connect(self.show_ai_button)
        self.update_ai_button_position()

        # Добавляем кнопку трекера заметок
        self.notes_button = NotesButtonUI(self)
        self.notes_button.clicked.connect(self.show_notes_button)
        self.update_notes_button_position()

        # Добавляем кнопку трекера привычек
        self.habits_button = HabitsButtonUI(self)
        self.habits_button.clicked.connect(self.show_habits_button)
        self.update_habits_button_position()

        # Добавляем кнопку достижений/статистики/прогресса
        self.achievements_button = AchievementsButtonUI(self)
        self.achievements_button.clicked.connect(self.show_achievements_button)
        self.update_achievements_button_position()

        # Добавляем кнопку информации
        self.info_button = InfoButtonUI(self)
        self.info_button.clicked.connect(self.show_info_dialog)
        self.update_info_button_position()

        # Добавляем кнопку настроек
        self.settings_button = SettingsButtonUI(self)
        self.settings_button.clicked.connect(self.show_settings_dialog)
        self.update_settings_button_position()

        # Подключаем обработчик изменения размеров окна
        self.resizeEvent = self.on_resize

        # Устанавливаем размеры окна
        self.showMaximized()


    def show_about_dialog(self):
        about_dialog = AboutDialogUI(self)
        about_dialog.show()
    

    def show_account_dialog(self):
        account_dialog = AccountDialogUI(self)
        account_dialog.exec()

    
    def show_ai_button(self):
        ai_dialog = AIDialogUI(self)
        ai_dialog.show()
    

    def show_habits_button(self):
        notification_dialog = HabitsDialogUI(self)
        notification_dialog.show()
    

    def show_notes_button(self):
        notes_dialog = NotesDialogUI(self)
        notes_dialog.show()
    

    def show_achievements_button(self):
        achievements_dialog = AchievementsDialogUI(self)
        achievements_dialog.exec()
    

    def show_info_dialog(self):
        info_dialog = InfoDialogUI(self)
        info_dialog.show()
    

    def show_settings_dialog(self):
        settings_dialog = SettingsDialogUI(self)
        settings_dialog.show()
    

    def update_ai_button_position(self):
        """Обновляет позицию кнопки AI"""
        # Получаем размеры окна
        window_width = self.width()
        window_height = self.height()

        # Вычисляем позицию кнопки
        button_width = self.ai_button.width()
        button_height = self.ai_button.height()
        x = window_width - button_width - 20
        y = window_height - button_height - 490

        # Устанавливаем пощицию кнопки
        self.ai_button.move(x, y)
    

    def update_habits_button_position(self):
        """Обновляет позицию кнопки трекера привычек."""
        # Получаем размеры окна
        window_width = self.width()
        window_height = self.height()

        # Вычисляем позицию кнопки
        button_width = self.habits_button.width()
        button_height = self.habits_button.height()
        x = window_width - button_width - 20
        y = window_height - button_height - 425

        # Устанавливаем пощицию кнопки
        self.habits_button.move(x, y)
    

    def update_notes_button_position(self):
        """Обновляет позицию кнопки заметок."""
        # Получаем размеры окна
        window_width = self.width()
        window_height = self.height()

        # Вычисляем позицию кнопки
        button_width = self.notes_button.width()
        button_height = self.notes_button.height()
        x = window_width - button_width - 20
        y = window_height - button_height - 360

        # Устанавливаем пощицию кнопки
        self.notes_button.move(x, y)
    

    def update_achievements_button_position(self):
        """Обновляет позицию кнопки достижений."""
        # Получаем размеры окна
        window_width = self.width()
        window_height = self.height()

        # Вычисляем позицию кнопки
        button_width = self.achievements_button.width()
        button_height = self.achievements_button.height()
        x = window_width - button_width - 20
        y = window_height - button_height - 165

        # Устанавливаем пощицию кнопки
        self.achievements_button.move(x, y)
    

    def update_info_button_position(self):
        """Обновляет позицию кнопки настроек."""
        # Получаем размеры окна
        window_width = self.width()
        window_height = self.height()

        # Вычисляем позицию кнопки
        button_width = self.info_button.width()
        button_height = self.info_button.height()
        x = window_width - button_width - 20
        y = window_height - button_height - 100

        # Устанавливаем позицию кнопки
        self.info_button.move(x, y)
    

    def update_settings_button_position(self):
        """Обновляет позицию кнопки настроек."""
        # Получаем размеры окна
        window_width = self.width()
        window_height = self.height()

        # Вычисляем позицию кнопки
        button_width = self.settings_button.width()
        button_height = self.settings_button.height()
        x = window_width - button_width - 20
        y = window_height - button_height - 35

        # Устанавливаем позицию кнопки
        self.settings_button.move(x, y)


    def on_resize(self, event):
        """Обрабатывает событие изменения размеров окна."""
        self.update_ai_button_position()
        self.update_habits_button_position()
        self.update_notes_button_position()
        self.update_achievements_button_position()
        self.update_info_button_position()
        self.update_settings_button_position()
        super().resizeEvent(event)
