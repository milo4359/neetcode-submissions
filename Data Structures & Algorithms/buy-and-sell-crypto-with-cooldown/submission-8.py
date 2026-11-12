class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] *2 for _ in range(n+1)]
        
        for i in range(n-2, -1, -1):
            skip = max(dp[i+1][0], dp[i+1][1])
            dp[i][0] = skip

            buy = dp[i+1][1] + (prices[i+1] - prices[i]) 
            sell = prices[i+1] - prices[i] + max(dp[i+2][0], dp[i+1][1])
            dp[i][1] = max(buy, sell)

        return max(dp[0][0], dp[0][1])
        