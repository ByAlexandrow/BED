import sys
from cx_Freeze import setup, Executable

# Определите зависимости
build_options = {
    "packages": [
        "PySide6",  # Основная библиотека для GUI
        "altgraph",  # Зависимость для PyInstaller (если используется)
        "cx_Logging",  # Логирование
        "lief",  # Для работы с бинарными файлами
        "packaging",  # Для управления версиями и зависимостями
        "pefile",  # Для работы с PE-файлами
        "shiboken6",  # Для работы с PySide6
    ],
    "include_files": [
        ("resources/background", "resources/background"),
        ("resources/favicon", "resources/favicon"),
        ("resources/icons", "resources/icons"),
        "resources/favicon/favicon.ico"
    ],
    "include_msvcr": True,  # Включает системные библиотеки
}

# Определите исполняемый файл
executables = [
    Executable(
        "main.py",  # Основной файл вашего приложения
        base="Win32GUI" if sys.platform == "win32" else None,  # Используйте "Win32GUI" для GUI-приложений на Windows
        target_name="BED",  # Имя исполняемого файла
        icon="resources/favicon/favicon.ico",  # Укажите путь к иконке
    )
]

# Настройка сборки
setup(
    name="BED",
    version="1.0",
    description="Better Every Day",
    options={"build_exe": build_options},
    executables=executables,
)
