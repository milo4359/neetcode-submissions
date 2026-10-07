class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        atl, pac = set(), set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def bfs(ocean):
            q = deque(ocean)
            while q: 
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in ocean:
                        q.append((nr, nc))
                        ocean.add((nr, nc))

        for c in range(len(heights[0])):
            atl.add((len(heights) - 1, c))
            pac.add((0, c))
        for r in range(len(heights)):
            atl.add((r, len(heights[0]) - 1))
            pac.add((r, 0))
        bfs(atl)
        bfs(pac)
        for (r, c) in atl:
            if (r, c) in pac: res.append([r, c])
        return res




