#!/bin/bash

# ============================================================
# Скрипт сборки проекта "Поиск чисел Кита"
# ============================================================

# Переходим в корневую папку проекта
cd "$(dirname "$0")/.." || exit 1

echo "=========================================="
echo "  Сборка проекта: Поиск чисел Кита"
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

# Очищаем папку сборки
echo "[STEP 1] Очистка папки сборки..."
rm -rf build/app/application
rm -rf build/distr

# Создаем структуру папок сборки
echo "[STEP 2] Создание структуры папок..."
mkdir -p build/app/application/src/module-kit
mkdir -p build/app/application/src/ui
mkdir -p build/distr

# Копируем исходные файлы
echo "[STEP 3] Копирование исходных файлов..."
cp src/module-kit/KitChecker.py build/app/application/src/module-kit/
cp src/module-kit/KitFinder.py build/app/application/src/module-kit/
cp src/module-kit/KitBenchmark.py build/app/application/src/module-kit/
cp src/ui/main.py build/app/application/src/ui/

# Создаем __init__.py файлы
echo "[STEP 4] Создание __init__.py файлов..."
touch build/app/application/src/module-kit/__init__.py
touch build/app/application/src/ui/__init__.py

# Создаем архив дистрибутива
echo "[STEP 5] Создание архива дистрибутива..."
cd build/app/application
zip -r ../../distr/application-1.0.0.zip .
cd ../..

echo ""
echo "=========================================="
echo "  Сборка завершена успешно!"
echo "=========================================="
echo ""
echo "  Готовые файлы:"
echo "  - build/app/application/  (готовая программа)"
echo "  - build/distr/application-1.0.0.zip  (архив)"
echo ""