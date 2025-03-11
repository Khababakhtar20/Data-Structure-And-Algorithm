class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for char,count in r.items():
            if count > m[char]:
                return False

        return True
        