@echo off
chcp 65001 >nul
REM ============================================================
REM Скрипт запуска тестов проекта "Поиск чисел Кита" (Windows)
REM ============================================================

REM Переходим в корень проекта (на уровень выше папки scripts)
cd /d "%~dp0\.." || exit /b 1

echo ==========================================
echo   Запуск тестов проекта
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

REM Проверяем наличие папки tests
if not exist "tests" (
    echo [WARNING] Папка tests не найдена. Создаем...
    mkdir tests
    type nul > tests\__init__.py
    echo [INFO] Папка tests создана. Добавьте тесты в эту папку.
    pause
    exit /b 0
)

REM Проверяем наличие тестовых файлов
if not exist "tests\test_kit_checker.py" (
    echo [ERROR] Не найден tests\test_kit_checker.py
    echo Добавьте тестовые файлы в папку tests.
    pause
    exit /b 1
)

REM Запускаем тесты
echo [STEP] Запуск тестов...
echo.
py -m unittest discover -s tests -v

REM Сохраняем код завершения
set EXIT_CODE=%errorlevel%

echo.
if %EXIT_CODE% equ 0 (
    echo ==========================================
    echo   Все тесты пройдены успешно!
    echo ==========================================
) else (
    echo ==========================================
    echo   Некоторые тесты провалились (код: %EXIT_CODE%)
    echo ==========================================
)

echo.
pause
exit /b %EXIT_CODE%