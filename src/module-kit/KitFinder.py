from KitChecker import KitChecker

class KitFinder:
    def __init__(self):
        self.checker = KitChecker()
    
    def ValidateRange(self, start, end):
        if start > end:
            raise ValueError("Начало не может быть больше конца")
        if start < 10 or end < 10:
            raise ValueError("Числа Кита начинаются с 10")
        return True
    
    def FindKitNumbers(self, start, end):
        numbers = []
        if self.ValidateRange(start, end):
            for i in range(start, end + 1):
                if self.checker.IsKitNumber(i):
                    numbers.append(i)
        return numbers