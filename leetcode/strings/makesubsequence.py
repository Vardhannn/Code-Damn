class Solution:
    def appendCharacters(self, s: str, t: str) -> str:
        count = 0
        x, y = 0, 0
        while x < len(s) and y < len(t):
            if s[x] == t[y]:
                x += 1
                y += 1
                count += 1
            else:

                x +=1
            
                
        return len(t) - count
    

sol = Solution()
print(sol.appendCharacters("coaching", "coding")) # 2