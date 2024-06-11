class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        return [value for value in arr2 for x in (range(arr1.count(value)))] +sorted([value for value in arr1 if value not in arr2])
