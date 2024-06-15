class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new = sorted(list(set(nums)))
        return max(new) if len(new) <= 2 else new[-3]
        
        
        
