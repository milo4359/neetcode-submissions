class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n-1, -1, -1):
            temp = defaultdict(int)
            for total, num in dp.items():
                temp[total-nums[i]] += num
                temp[total+nums[i]] += num
            dp = temp

        return dp[target]
            
