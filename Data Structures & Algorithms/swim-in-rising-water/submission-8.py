class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while heap:
            t, i, j = heapq.heappop(heap)
            if (i, j) == (n - 1, n - 1): return t
            if(i, j) in visited: continue
            visited.add((i, j))
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(grid[nr][nc], t), nr, nc))
        

            

