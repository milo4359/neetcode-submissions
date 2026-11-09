class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices)+2)

        for i in range(len(prices)-2, -1,-1):
            dp[i] = max(prices[i+1] - prices[i] + dp[i+1], dp[i+2], dp[i+3], 0)

        return max(dp[0], dp[1])
        