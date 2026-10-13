@echo off
chcp 65001 >nul
REM ============================================================
REM Скрипт запуска проекта "Поиск чисел Кита" (Windows)
REM ============================================================

REM Переходим в корень проекта (на уровень выше папки scripts)
cd /d "%~dp0\.." || exit /b 1

echo ==========================================
echo   Запуск программы: Поиск чисел Кита
echo ==========================================
echo.
echo [INFO] Текущая папка: %CD%
echo.

REM Проверяем наличие Python (используем py - Python Launcher)
py --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python не найден! Установите Python с python.org
    pause
    exit /b 1
)

echo [INFO] Python найден:
py --version
echo.

REM Проверяем, что главный файл на месте
if not exist "src\ui\main.py" (
    echo [ERROR] Не найден src\ui\main.py
    echo Проверьте структуру проекта.
    pause
    exit /b 1
)

REM Запускаем программу
echo [INFO] Запуск программы...
echo.
py src\ui\main.py

REM Сохраняем код завершения
set EXIT_CODE=%errorlevel%

echo.
if %EXIT_CODE% equ 0 (
    echo [INFO] Программа завершена успешно.
) else (
    echo [ERROR] Программа завершилась с ошибкой (код: %EXIT_CODE%).
)

echo.
pause
exit /b %EXIT_CODE%