class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smal, larg = min(strs), max(strs)

        for x in range(len(smal)):
            if smal[x]!=larg[x]:
                return smal[:x]
        return smal