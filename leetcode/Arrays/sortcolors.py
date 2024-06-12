class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [nums.count(x) for x in range(3)]
        j = 0
        x = 0
        for i in range(3):
            
            while x < colors[i]:
                nums[j] = i
                j += 1
                x += 1
            x = 0