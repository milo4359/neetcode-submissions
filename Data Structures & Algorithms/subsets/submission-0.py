class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [set()]
        for num in nums: res.append({num})
        for i in range(len(res)):
            for j in range(len(res)):
                if res[i] | res[j] not in res: res.append(res[i] | res[j])
        return [list(x) for x in res]