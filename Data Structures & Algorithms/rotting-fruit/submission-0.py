class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        ones = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: ones += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((0,1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        ones -= 1
                        q.append((nr, nc))
            if q: count += 1
        
        
        return count if ones == 0 else -1