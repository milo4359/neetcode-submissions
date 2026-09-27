class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        def dfs(i):
            if i == len(nums):
                if current[:] not in res: res.append(current[:])
                return
            current.append(nums[i])
            dfs(i + 1)
            current.pop()
            dfs(i + 1)
        dfs(0)
        return res
