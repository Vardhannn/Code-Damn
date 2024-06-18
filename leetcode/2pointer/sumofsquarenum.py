class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)

        while i <= j:
            square = i ** 2 + j ** 2
            print(i,j)
            if square == c:
                return True
            if square < c:
                i += 1
            else:
                j -= 1
        return False
    
sol = Solution()
print(sol.judgeSquareSum(4))