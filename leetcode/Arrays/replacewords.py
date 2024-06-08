
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort()
        words = sentence.split()
        for x in range(len(words)):
            for y in range(len(dictionary)):
                if words[x].startswith(dictionary[y]):
                    words[x] = dictionary[y]
                    break
            
        return " ".join(words)


    

sol = Solution()
print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs")) # "the cat was rat by the bat"