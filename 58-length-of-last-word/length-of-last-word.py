class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        test=s
        last_w=len(test.strip().split()[-1])
        return last_w