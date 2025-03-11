class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = []
        for i in range (len(nums)+1):
            if i not in arr:
                arr.append(i)

        for i in arr:
            if i not in nums:
                return i
