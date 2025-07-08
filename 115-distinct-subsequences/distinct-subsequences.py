class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        def count(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                case1 = count(i + 1, j + 1)
                case2 = count(i + 1, j)
                dp[i][j] = case1 + case2
            else:
                dp[i][j] = count(i + 1, j)
            return dp[i][j]

        return count(0, 0)
