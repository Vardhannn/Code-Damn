class Solution:
    def longestPalindrome(self, s: str) -> int:

        arr = set(st for st in s)
        countarray = [s.count(x) for x in arr]

        oddcount = sum([1 for x in countarray if x%2 != 0])
        if oddcount > 0:    
            return sum([x if x%2 == 0 else x-1 for x in countarray]) + 1
        else:
            return sum([x if x%2 == 0 else x-1 for x in countarray])


    
sol = Solution()
print(sol.longestPalindrome("a")) # 7
    