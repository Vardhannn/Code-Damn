class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        hashmap = sorted(zip(difficulty, profit))

        worker.sort()

        j = 0
        total_profit = 0
        max_profit = 0
        for i in range(len(worker)):
            while j < len(difficulty) and worker[i] >= hashmap[j][0]:
                max_profit = max(max_profit, hashmap[j][1])
                j += 1
            total_profit = max_profit + total_profit

        return (total_profit)