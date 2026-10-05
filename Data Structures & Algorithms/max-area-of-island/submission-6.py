class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        q = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = 1
                    grid[i][j] = 0
                    q.append((i, j))
                    while q:
                        r, c = q.popleft()
                        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            nr, nc = dr + r, dc + c
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                                count += 1
                    res = max(res, count)

        return res

