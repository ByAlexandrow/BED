# installer.nsi

# Название приложения
Name "Better Every Day"

# Имя выходного файла
OutFile "Setup_BED.exe"

# Папка для установки
InstallDir "$PROGRAMFILES\BED"

# Страница выбора папки
Page directory
Page instfiles

# Установка
Section "Install"
    # Создаем папку
    SetOutPath "$INSTDIR"

    # Копируем все файлы из папки сборки
    File /r "D:\Dev\BED\build\exe.win-amd64-3.11\*.*"

    # Создаем ярлык на рабочем столе
    CreateShortcut "$DESKTOP\BED.lnk" "$INSTDIR\BED.exe" "$INSTDIR\resources\favicon\favicon.ico"

    # Добавляем в меню "Пуск"
    CreateDirectory "$SMPROGRAMS\BED"
    CreateShortcut "$SMPROGRAMS\BED\BED.lnk" "$INSTDIR\BED.exe" "$INSTDIR\resources\favicon\favicon.ico"

    # Создаем файл удаления
    WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

# Удаление
Section "Uninstall"
    # Удаляем все файлы
    Delete "$INSTDIR\*.*"

    # Удаляем папку установки
    RMDir "$INSTDIR"

    # Удаляем ярлык с рабочего стола
    Delete "$DESKTOP\BED.lnk"

    # Удаляем ярлык из меню "Пуск"
    Delete "$SMPROGRAMS\BED\BED.lnk"
    RMDir "$SMPROGRAMS\BED"

    # Удаляем файл удаления
    Delete "$INSTDIR\uninstall.exe"
SectionEnd