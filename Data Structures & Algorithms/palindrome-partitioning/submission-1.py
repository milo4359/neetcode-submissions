class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        strs = []
        def dfs(i, substring):
            if i == len(s):
                if not substring: res.append(strs[:])
                return
            substring += s[i]
            if palindrome(substring): 
                strs.append(substring)
                dfs(i + 1, "")
                strs.pop()
            dfs(i + 1, substring)

        def palindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]: return False
            return True
        
        dfs(0, "")
        return res
