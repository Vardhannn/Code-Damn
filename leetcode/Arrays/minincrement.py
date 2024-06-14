class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        count = increment = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                increment = (nums[i-1] + 1) - nums[i]
                nums[i] = nums[i] + increment
                count = count + increment
        return count 

        