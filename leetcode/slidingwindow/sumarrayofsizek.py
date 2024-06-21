class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        seen = set()
        left = 0
        right = 0
        arrsum = 0
        max_sum = 0

        while right < len(nums):

            while nums[right] in seen:
                arrsum -= nums[left]
                seen.remove(nums[left])
                left += 1

            arrsum += nums[right]
            seen.add(nums[right])
            if (right - left + 1) == k:
                max_sum = max(max_sum, arrsum)
                arrsum -= nums[left]
                seen.remove(nums[left])
                left += 1


            right += 1

        return max_sum

