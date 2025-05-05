from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        count_array = [0] * 101  # Assuming nums contains integers in the range [1, 100]
        
        for num in nums:
            count_array[num] += 1  # Increment count for the current number
        
        for count in count_array:
            pairs += (count * (count - 1)) // 2  # Calculate pairs using nC2 formula
        
        return pairs

