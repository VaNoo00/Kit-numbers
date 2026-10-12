import sys
import os
import unittest

# Добавляем путь к модулю module-kit
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'module-kit'))

from KitFinder import KitFinder


class TestKitFinder(unittest.TestCase):
    
    def setUp(self):
        """Создаем экземпляр KitFinder перед каждым тестом"""
        self.finder = KitFinder()
    
    # ===== Тесты на нормальный поиск =====
    
    def test_find_keith_numbers_10_to_100(self):
        """Тест: поиск чисел Кита от 10 до 100"""
        result = self.finder.FindKitNumbers(10, 100)
        expected = [14, 19, 28, 47, 61, 75]
        self.assertEqual(result, expected)
    
    def test_find_keith_numbers_100_to_200(self):
        """Тест: поиск чисел Кита от 100 до 200"""
        result = self.finder.FindKitNumbers(100, 200)
        self.assertIn(197, result)
    
    def test_find_keith_numbers_10_to_1000(self):
        result = self.finder.FindKitNumbers(10, 1000)
        self.assertIn(14, result)
        self.assertIn(197, result)
        self.assertIn(742, result)  # ← 742 — реальное число Кита
    
    def test_find_single_keith_number(self):
        """Тест: поиск одного числа Кита (197)"""
        result = self.finder.FindKitNumbers(197, 197)
        self.assertEqual(result, [197])
    
    def test_find_no_keith_numbers(self):
        """Тест: диапазон без чисел Кита"""
        result = self.finder.FindKitNumbers(10, 13)
        self.assertEqual(result, [])
    
    # ===== Тесты на некорректные диапазоны =====
    
    def test_start_greater_than_end_raises_error(self):
        """Тест: start > end должно вызывать ValueError"""
        with self.assertRaises(ValueError) as context:
            self.finder.FindKitNumbers(100, 10)
        self.assertIn("Начало не может быть больше конца", str(context.exception))
    
    def test_start_less_than_10_raises_error(self):
        """Тест: start < 10 должно вызывать ValueError"""
        with self.assertRaises(ValueError) as context:
            self.finder.FindKitNumbers(5, 100)
        self.assertIn("Числа Кита начинаются с 10", str(context.exception))
    
    def test_end_less_than_10_raises_error(self):
        """Тест: end < 10 должно вызывать ValueError"""
        with self.assertRaises(ValueError) as context:
            self.finder.FindKitNumbers(5, 9)  # ← start <= end, но оба < 10
        self.assertIn("Числа Кита начинаются с 10", str(context.exception))
        
    def test_both_less_than_10_raises_error(self):
        """Тест: оба числа < 10 должны вызывать ValueError"""
        with self.assertRaises(ValueError) as context:
            self.finder.FindKitNumbers(1, 9)
        self.assertIn("Числа Кита начинаются с 10", str(context.exception))
    
    # ===== Тесты на граничные случаи =====
    
    def test_find_at_exact_boundary_10(self):
        """Тест: поиск начиная с 10"""
        result = self.finder.FindKitNumbers(10, 20)
        self.assertIn(14, result)
        self.assertIn(19, result)
    
    def test_find_large_range(self):
        """Тест: поиск в большом диапазоне (производительность)"""
        # Этот тест проверяет, что программа не зависает
        result = self.finder.FindKitNumbers(10, 10000)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
    
    def test_result_is_sorted(self):
        """Тест: результаты должны быть отсортированы по возрастанию"""
        result = self.finder.FindKitNumbers(10, 1000)
        self.assertEqual(result, sorted(result))
    
    def test_result_contains_only_unique_numbers(self):
        """Тест: результаты не должны содержать дубликатов"""
        result = self.finder.FindKitNumbers(10, 1000)
        self.assertEqual(len(result), len(set(result)))


if __name__ == '__main__':
    unittest.main()