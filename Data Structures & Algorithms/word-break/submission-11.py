class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for w in words:
                if i + len(w) <= len(s) and w == s[i:i+len(w)]:
                    dp[i] = dp[i+len(w)]
                    if dp[i]: break
        return dp[0]
            