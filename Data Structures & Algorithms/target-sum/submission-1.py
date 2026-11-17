class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[n][0] = 1

        for i in range(n-1, -1, -1):
            
            for total, num in dp[i+1].items():
                dp[i][total-nums[i]] += num
                dp[i][total+nums[i]] += num

        return dp[0][target]
            
