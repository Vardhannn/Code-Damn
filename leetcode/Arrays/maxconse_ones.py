class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        ans = 0

        for x in range(len(nums)):

            if nums[x] == 0:
                count = 0

            else:
                count += 1
                ans = max(count, ans)
        return ans