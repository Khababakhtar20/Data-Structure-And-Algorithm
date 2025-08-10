from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:  # Fix: Compare with val directly
                nums[l] = nums[i]
                l += 1
        return l
