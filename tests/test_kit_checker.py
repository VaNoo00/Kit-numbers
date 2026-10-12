import sys
import os
import unittest

# Добавляем путь к модулю module-kit
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'module-kit'))

from KitChecker import KitChecker


class TestKitChecker(unittest.TestCase):
    
    def setUp(self):
        """Создаем экземпляр KitChecker перед каждым тестом"""
        self.checker = KitChecker()
    
    # ===== Тесты на числа Кита =====
    
    def test_14_is_keith_number(self):
        """Тест: 14 должно быть числом Кита"""
        self.assertTrue(self.checker.IsKitNumber(14))
    
    def test_19_is_keith_number(self):
        """Тест: 19 должно быть числом Кита"""
        self.assertTrue(self.checker.IsKitNumber(19))
    
    def test_28_is_keith_number(self):
        """Тест: 28 должно быть числом Кита"""
        self.assertTrue(self.checker.IsKitNumber(28))
    
    def test_47_is_keith_number(self):
        """Тест: 47 должно быть числом Кита"""
        self.assertTrue(self.checker.IsKitNumber(47))
    
    def test_61_is_keith_number(self):
        """Тест: 61 должно быть числом Кита"""
        self.assertTrue(self.checker.IsKitNumber(61))
    
    def test_75_is_keith_number(self):
        """Тест: 75 должно быть числом Кита"""
        self.assertTrue(self.checker.IsKitNumber(75))
    
    def test_197_is_keith_number(self):
        """Тест: 197 должно быть числом Кита (трехзначное)"""
        self.assertTrue(self.checker.IsKitNumber(197))
    

    # Стало (правильно):
    def test_742_is_keith_number(self):
        """Тест: 742 должно быть числом Кита (трехзначное)"""
        self.assertTrue(self.checker.IsKitNumber(742))
    
    # ===== Тесты на НЕ числа Кита =====
    
    def test_10_is_not_keith_number(self):
        """Тест: 10 не должно быть числом Кита"""
        self.assertFalse(self.checker.IsKitNumber(10))
    
    def test_15_is_not_keith_number(self):
        """Тест: 15 не должно быть числом Кита"""
        self.assertFalse(self.checker.IsKitNumber(15))
    
    def test_100_is_not_keith_number(self):
        """Тест: 100 не должно быть числом Кита"""
        self.assertFalse(self.checker.IsKitNumber(100))
    
    def test_999_is_not_keith_number(self):
        """Тест: 999 не должно быть числом Кита"""
        self.assertFalse(self.checker.IsKitNumber(999))
    
    # ===== Граничные случаи =====
    
    def test_single_digit_returns_false(self):
        """Тест: однозначные числа не являются числами Кита"""
        for i in range(1, 10):
            self.assertFalse(self.checker.IsKitNumber(i))
    
    def test_zero_returns_false(self):
        """Тест: 0 не является числом Кита"""
        self.assertFalse(self.checker.IsKitNumber(0))
    
    def test_negative_number_returns_false(self):
        """Тест: отрицательные числа не являются числами Кита"""
        self.assertFalse(self.checker.IsKitNumber(-10))
        self.assertFalse(self.checker.IsKitNumber(-100))
        self.assertFalse(self.checker.IsKitNumber(-1))
    
    def test_numbers_below_10_return_false(self):
        """Тест: все числа меньше 10 возвращают False"""
        for i in range(-100, 10):
            self.assertFalse(self.checker.IsKitNumber(i))


if __name__ == '__main__':
    unittest.main()