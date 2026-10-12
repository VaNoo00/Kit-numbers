import time
from KitFinder import KitFinder

class KitBenchmark:
    def __init__(self):
        self.finder = KitFinder()
        self.found_numbers = []
        self.execution_time = 0.0
        self.last_start = None
        self.last_end = None
    
    def Run(self, start, end):
        self.last_start = start
        self.last_end = end
        start_time = time.perf_counter()
        self.found_numbers = self.finder.FindKitNumbers(start, end)
        end_time = time.perf_counter()
        self.execution_time = end_time - start_time
    
    def GetResults(self):
        result = (f"начало: {self.last_start}\n"
                  f"конец: {self.last_end}\n"
                  f"время выполнения: {self.execution_time:.6f} сек\n"
                  f"количество чисел Кита: {len(self.found_numbers)}\n"
                  f"Числа Кита: {self.found_numbers.copy()}")
        return result