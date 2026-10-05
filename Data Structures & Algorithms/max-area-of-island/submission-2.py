class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        q = deque()
        def bfs(r, c):
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] != 1: return 0
            q.append((r, c))
            grid[r][c] = 0
            count = 0
            r, c, = q.popleft()
            for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                nr, nc = dr + r, dc + c
                count += bfs(nr, nc)
            return count + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = bfs(i, j) 
                    if count > res: res = count

        return res

