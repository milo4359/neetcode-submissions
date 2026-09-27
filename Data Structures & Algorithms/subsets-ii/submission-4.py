class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        def dfs(i):
            if i == len(nums):
                res.append(current[:])
                return
            current.append(nums[i])
            dfs(i + 1)
            current.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]: j += 1
            dfs(j)
        dfs(0)
        return res
