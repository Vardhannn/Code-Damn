from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        
        max_num = deque()
        min_num = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):

            while max_num and max_num[-1] < nums[right]:
                max_num.pop()
            max_num.append(nums[right])

            while min_num and min_num[-1] > nums[right]:
                min_num.pop()
            min_num.append(nums[right])

            while max_num[0] - min_num[0] > limit:

                if max_num[0] == nums[left]:
                    max_num.popleft()
                if min_num[0] == nums[left]:
                    min_num.popleft()

                left += 1

            max_length = max(max_length, right - left + 1)
        
        return max_length