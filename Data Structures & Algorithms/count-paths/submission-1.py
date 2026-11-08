class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i + 1 < m: grid[i+1][j] += grid[i][j]
                if j + 1 < n: grid[i][j+1] += grid[i][j]

        return grid[m-1][n-1]