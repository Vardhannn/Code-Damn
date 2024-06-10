class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        rem = {0: 1}
        cum_sum = 0
        count = 0

        for i in range(len(nums)):
            cum_sum = (cum_sum + nums[i]) % k
            if cum_sum < 0:
                cum_sum += k

            if cum_sum in rem:
                count += rem[cum_sum]
                rem[cum_sum] += 1
            else:
                rem[cum_sum] = 1
        return count