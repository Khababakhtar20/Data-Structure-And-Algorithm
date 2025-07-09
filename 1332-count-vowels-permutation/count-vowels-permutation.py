class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels_map = {
            'a':['e'],
            'e':['a','i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a'],
        }
        MOD = 10**9 +7
        @lru_cache(None)
        def dfs(vowel,length):
            if length == 1:
                return 1 
            total = 0
            for nei in vowels_map[vowel]:
                total = (total + dfs(nei,length-1)) % MOD
            return total

        result = 0
        for ch in 'aeiou':
            result = (result + dfs (ch,n)) % MOD
        return result 


