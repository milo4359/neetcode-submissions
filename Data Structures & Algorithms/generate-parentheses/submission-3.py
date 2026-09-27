class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = ""
        def dfs(i):
            nonlocal string
            if i > n or len(string) - i > i: return
            if i == n and len(string) == n*2:  
                res.append(string)
                return
            string += '('
            dfs(i + 1)
            string = string[:-1]
            string += ')'
            dfs(i)
            string = string[:-1]

        dfs(0)
        return res

