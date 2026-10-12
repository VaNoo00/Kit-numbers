class KitChecker:
    def IsKitNumber(self, number):
        if(number >= 10):
            digits = self.GetDigits(number)
            return self.CumulativeSum(digits, number)
        else:
            return False
        
    def GetDigits(self, number):
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10
        return digits[::-1]
    
    def CumulativeSum(self, digits, number):
        sum_num = 0
        len_num = len(str(number))
        while(sum_num < number):
            sum_num = sum(digits[-len_num:])
            for i in range(len_num-1):
                digits[i] = digits[i+1]
            digits[-1] = sum_num
        if sum_num == number:
            return True
        else:
            return False
            