class Solution:
    def addDigits(self, num: int) -> int:
        return self.sumof(num)

    def sumof(self, num):
        if num < 9:
            return num
        digit = sum([int(x) for x in str(num)])

        while digit > 9:
            digit = sum([int(x) for x in str(digit)])
        return digit

############################################################################################################

class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 1 + (num - 1) % 9