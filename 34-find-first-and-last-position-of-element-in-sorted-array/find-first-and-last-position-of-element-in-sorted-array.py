from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        return [first, last]

    def findFirst(self, nums: List[int], target: int) -> int:
        start, end, index = 0, len(nums) - 1, -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
            if nums[mid] == target:
                index = mid
        return index

    def findLast(self, nums: List[int], target: int) -> int:
        start, end, index = 0, len(nums) - 1, -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
            if nums[mid] == target:
                index = mid
        return index
