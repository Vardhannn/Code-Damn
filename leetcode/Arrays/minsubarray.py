class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        prefix_sum = 0
        ans = float('inf')
        
        for i in range(len(nums)):
            prefix_sum += nums[i]

            while prefix_sum >= target:
                ans  = min(ans, i-left+1)
                prefix_sum -= nums[left]
                left += 1
                
        return ans if ans != float('inf') else 0
            
            