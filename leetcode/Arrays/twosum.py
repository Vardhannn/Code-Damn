class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[y] == target - nums[x]:
                    return [x, y]


sol = Solution()
print(sol.twoSum([3, 3], 6)) # [0, 1]