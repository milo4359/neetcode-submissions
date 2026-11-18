class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            temp = defaultdict(int)
            for total, count in dp.items():
                temp[total-num] += count
                temp[total+num] += count
            dp = temp

        return dp[target]
            
