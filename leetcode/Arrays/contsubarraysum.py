class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        rem = {0: -1}
        cum_sum = 0

        for i in range(len(nums)):
            cum_sum = (cum_sum + nums[i]) % k

            if cum_sum in rem:
                if i - rem[cum_sum] > 1:
                    return True
            else:
                rem[cum_sum] = i
        return False