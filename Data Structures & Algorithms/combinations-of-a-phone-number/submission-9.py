class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        letters = "abcdefghijklmnopqrstuvwxyz"
        res = []
        def dfs(i, s):
            if len(s) == len(digits):
                res.append(s)
                return
            paths = 4 if int(digits[i]) == 7 or int(digits[i]) == 9 else 3
            add = 1 if int(digits[i]) > 7 else 0
            for j in range(paths):
                dfs(i + 1, s + letters[3*(int(digits[i]) - 2) + j + add])

        dfs(0, "")
        return res