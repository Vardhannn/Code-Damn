class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(n):
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        if n < 3:
            return 2
        if 7 < n <= 11:
            return 11
        i = 2
        while True:
            num = int(str(i) + str(i)[::-1][1:])
            if num >= n and isPrime(num): 
                return num
            i += 1