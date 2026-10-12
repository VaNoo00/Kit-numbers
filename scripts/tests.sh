#!/bin/bash

# ============================================================
# Скрипт запуска тестов проекта "Поиск чисел Кита"
# ============================================================

# Переходим в корневую папку проекта
cd "$(dirname "$0")/.." || exit 1

echo "=========================================="
echo "  Запуск тестов проекта"
echo "=========================================="
echo ""

# Проверяем наличие Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "[ERROR] Python не найден! Установите Python."
    exit 1
fi

echo "[INFO] Python найден: $($PYTHON_CMD --version)"
echo ""

# Проверяем наличие папки tests
if [ ! -d "tests" ]; then
    echo "[WARNING] Папка tests не найдена. Создаем..."
    mkdir -p tests
    touch tests/__init__.py
    echo "[INFO] Папка tests создана. Добавьте тесты в эту папку."
    exit 0
fi

# Запускаем тесты
echo "[STEP] Запуск тестов..."
echo ""
$PYTHON_CMD -m unittest discover -s tests -v

# Сохраняем код завершения
EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo "=========================================="
    echo "  Все тесты пройдены успешно!"
    echo "=========================================="
else
    echo "=========================================="
    echo "  Некоторые тесты провалились (код: $EXIT_CODE)"
    echo "=========================================="
fi

echo ""
exit $EXIT_CODE