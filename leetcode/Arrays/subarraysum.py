class Solution:
    def checkSubarraySum(self, nums, k):
        count = 0
        for x in range(len(nums)):
            print("x: ", x)
            for y in range(x+1,len(nums)+1):
                print(nums[x:y])
                s = sum(nums[x:y])
                if s % k == 0:
                    count += 1

        return count



sol = Solution()
print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))
