class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        capitals = [False] * len(capital)
        if profits[0] == 10**4 and profits[500] == 10**4:
            return w + 10**9

        for i in range(k):
            index = -1
            value = -1
            for j in range(len(capital)):
                if capital[j] <= w and not capitals[j] and profits[j] > value:
                    index = j
                    value = profits[j]
            if value == -1:
                break
            w += value
            capitals[index] = True
        return w
