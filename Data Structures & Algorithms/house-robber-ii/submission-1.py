class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        def money(array):
            prev, curr = 0, 0
            for num in array:
                prev, curr = curr, max(curr, prev + num)
            return curr

        return max(money(nums[1:]), money(nums[:-1]))

