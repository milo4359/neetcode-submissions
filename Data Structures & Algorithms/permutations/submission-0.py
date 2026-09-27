class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        def dfs():
            if len(current) == len(nums):
                res.append(current[:])
                return
            for i in range(len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    dfs()
                    current.pop()
        dfs()
        return res