class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for c in s:
            for i in range(n, 0, -1):
                if c == t[i-1]: dp[i] += dp[i-1]

        return dp[n] 