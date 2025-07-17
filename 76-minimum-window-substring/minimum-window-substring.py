from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = defaultdict(int)
        for letter in t:
            freqT[letter] += 1

        lettersToSatisfy = len(freqT)
        left = 0
        right = float('inf')
        i = 0
        
        for j, char in enumerate(s):
            if char in freqT:
                freqT[char] -= 1
                if freqT[char] == 0:
                    lettersToSatisfy -= 1

            while lettersToSatisfy == 0:
                if j - i < right - left:
                    left, right = i, j

                if s[i] in freqT:
                    freqT[s[i]] += 1
                    if freqT[s[i]] > 0:
                        lettersToSatisfy += 1
                i += 1

        return "" if right == float('inf') else s[left:right+1]
