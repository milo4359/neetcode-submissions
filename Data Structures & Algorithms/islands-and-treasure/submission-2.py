class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        if not grid or not grid[0]:
            return
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for i in range(rows):                 # seed EVERY gate into the queue
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1   # first arrival = shortest; mark on push
                    q.append((nr, nc))

