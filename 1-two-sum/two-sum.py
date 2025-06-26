class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}  # Dictionary to store numbers and their indices
        n = len(nums)

        for i in range(n):  # Iterate through the list
            complement = target - nums[i]  # Calculate complement
            
            if complement in numMap:  # Check if complement exists in dictionary
                return [numMap[complement], i]  # Return indices of the two numbers
            
            numMap[nums[i]] = i  # Store the number with its index in dictionary

        return []  # No solution found

     
