#!/bin/bash

# ============================================================
# Скрипт запуска программы "Поиск чисел Кита"
# ============================================================

# Переходим в корневую папку проекта (на уровень выше папки scripts)
# $0 — путь к самому скрипту
# dirname $0 — папка, где лежит скрипт (scripts/)
# cd .. — поднимаемся на уровень вверх (в application/)
cd "$(dirname "$0")/.." || exit 1

echo "=========================================="
echo "  Запуск программы: Поиск чисел Кита"
echo "=========================================="
echo ""

# Проверяем, установлен ли Python 3
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Ошибка: Python не найден!"
    echo "   Установите Python 3 и добавьте его в PATH."
    exit 1
fi

echo "✅ Используется: $($PYTHON_CMD --version)"
echo ""

# Запускаем главный файл программы
$PYTHON_CMD src/ui/main.py

# Сохраняем код завершения программы
EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Программа завершена успешно."
else
    echo "❌ Программа завершена с ошибкой (код: $EXIT_CODE)."
fi

exit $EXIT_CODE