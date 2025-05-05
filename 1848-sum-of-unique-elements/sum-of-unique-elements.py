class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = []   # List to store unique numbers (those that appear only once)
        d = {}        # Dictionary to store the frequency count of each number in nums
        
        # First loop: Counting the occurrences of each number in nums
        for i in nums:
            if i in d:         # If the number i is already in the dictionary
                d[i] += 1      # Increment its count by 1
            else:
                d[i] = 1       # If the number i is not in the dictionary, initialize its count to 1
        
        # Second loop: Identifying the unique numbers (those that appear only once)
        for key, val in d.items():   # Iterating through the dictionary to check frequency
            if val == 1:             # If the number appears only once
                unique.append(key)   # Add it to the unique list
        
        # Finally, summing up the unique numbers
        return sum(unique)           # Return the sum of the numbers that appear only once
