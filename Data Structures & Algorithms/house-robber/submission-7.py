class Solution:
    def rob(self, nums: List[int]) -> int: 
        n = len(nums)
        if n < 2: return max(nums)
        money = [0] * n
        money[0], money[1] = nums[0], nums[1]
        for i in range(2, n):
            money[i] = nums[i] + max(money[i-2], money[i-3])
        
        return max(money[n-1], money[n-2])