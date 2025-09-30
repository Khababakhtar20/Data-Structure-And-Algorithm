class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        res = letters[0]  # Default answer is the first letter (wrap-around case)

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                # letters[mid] is greater than target, so it's a valid candidate
                res = letters[mid]
                right = mid - 1  # but maybe there's a smaller valid one on the left
            else:
                # letters[mid] <= target, not valid → search in the right half
                left = mid + 1

        return res
