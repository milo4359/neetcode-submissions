class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        res = 0

        def dfs(r, c):
            nonlocal res
            if dp[r][c] != 1: return dp[r][c]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            best = 0
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] > matrix[r][c]: 
                    dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))
                    best = max(best, dp[r][c])
            res = max(res, best)
            return best
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if dp[r][c] == 1: dfs(r, c)
                
        return res + 1
        



