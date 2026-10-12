import sys
import os

module_kit_path = os.path.join(os.path.dirname(__file__), '..', 'module-kit')
sys.path.insert(0, module_kit_path)

from KitBenchmark import KitBenchmark

def main():
    print("========Поиск чисел Кита===========\n")
    benchmark = KitBenchmark()
    print("Введите диапазон чисел (минимально от 10):")
    try:
        start = int(input("Начало: "))
        end = int(input("Конец: "))
        print()
        benchmark.Run(start, end)
        print(benchmark.GetResults())
        print()
    except ValueError as e:
        print(f"Ошибка! {e}")

if __name__ == "__main__":
    main()