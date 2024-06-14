class Solution:
    def maxArea(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1
        area = 0
        mh = max(height)
        while left < right:
            max_area = min(height[left], height[right]) * (right - left)
            area = max(area, max_area)

            if mh * (right - left) <= area:
                break

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
            
        