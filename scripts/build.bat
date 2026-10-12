@echo off
chcp 65001 >nul
REM ============================================================
REM Скрипт сборки проекта "Поиск чисел Кита" (Windows)
REM ============================================================

REM Переходим в корень проекта (на уровень выше папки scripts)
cd /d "%~dp0.." || exit /b 1

echo ==========================================
echo   Сборка проекта: Поиск чисел Кита
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

REM Проверяем, что исходные файлы на месте
if not exist "src\module-kit\KitChecker.py" (
    echo [ERROR] Не найден src\module-kit\KitChecker.py
    echo Проверьте структуру проекта.
    pause
    exit /b 1
)

if not exist "src\ui\main.py" (
    echo [ERROR] Не найден src\ui\main.py
    pause
    exit /b 1
)

REM Очищаем папку сборки
echo [STEP 1] Очистка папки сборки...
if exist "build" (
    rmdir /s /q "build"
)

REM Создаём структуру папок сборки
echo [STEP 2] Создание структуры папок...
mkdir "build\app\Kit-numbers\src\module-kit"
mkdir "build\app\Kit-numbers\src\ui"
mkdir "build\distr"

REM Копируем исходные файлы
echo [STEP 3] Копирование исходных файлов...
copy "src\module-kit\KitChecker.py"   "build\app\Kit-numbers\src\module-kit\" >nul
copy "src\module-kit\KitFinder.py"    "build\app\Kit-numbers\src\module-kit\" >nul
copy "src\module-kit\KitBenchmark.py" "build\app\Kit-numbers\src\module-kit\" >nul
copy "src\ui\main.py"                 "build\app\Kit-numbers\src\ui\" >nul

REM Создаём __init__.py
echo [STEP 4] Создание __init__.py файлов...
type nul > "build\app\Kit-numbers\src\module-kit\__init__.py"
type nul > "build\app\Kit-numbers\src\ui\__init__.py"

REM Копируем корневые файлы
echo [STEP 5] Копирование документации...
copy "README.md" "build\app\Kit-numbers\" >nul
copy "LICENSE"   "build\app\Kit-numbers\" >nul
copy "INSTALL"   "build\app\Kit-numbers\" >nul

REM Создаём архив дистрибутива
echo [STEP 6] Создание архива дистрибутива...
powershell -Command "Compress-Archive -Path 'build\app\Kit-numbers\*' -DestinationPath 'build\distr\Kit-numbers-1.0.0.zip' -Force"

echo.
echo ==========================================
echo   Сборка завершена успешно!
echo ==========================================
echo.
echo   Готовые файлы:
echo   - build\app\Kit-numbers\
echo   - build\distr\Kit-numbers-1.0.0.zip
echo.
pause