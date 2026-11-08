class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True                       # empty prefix is reachable
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:   # reachable at j, and s[j:i] is a word
                    dp[i] = True
                    break                   # one valid split is enough
        return dp[n]
            