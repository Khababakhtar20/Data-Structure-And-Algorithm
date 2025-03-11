from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0  # Set current digit to 0 if it's 9
            else:
                digits[i] += 1  # Increment and return if not 9
                return digits
        
        # If all digits were 9, prepend 1
        return [1] + digits
