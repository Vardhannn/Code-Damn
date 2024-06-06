class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0 and m > 0:
            nums1 = sorted(nums1[:n]+nums2)
            print(nums1)
        elif m == 0:
            nums1 = nums2

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # [1,2,2,3,5,6]