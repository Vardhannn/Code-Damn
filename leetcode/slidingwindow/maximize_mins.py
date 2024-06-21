class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        
        unsatisfied = 0

        for i in range(minutes):
            unsatisfied += customers[i] * grumpy[i]

        max_unsatisfied = unsatisfied

        for i in range(minutes, len(customers)):

            unsatisfied += customers[i] * grumpy[i]
            unsatisfied -= customers[i - minutes] * grumpy[i - minutes]

            max_unsatisfied = max(unsatisfied, max_unsatisfied)

        total = max_unsatisfied

        for i in range(len(customers)):
            total += customers[i] * (1 - grumpy[i])

        return total