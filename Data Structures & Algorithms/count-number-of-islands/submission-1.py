class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    stack.append((i, j))
                    while stack:
                        r, c = stack.pop()
                        grid[r][c] = "#"
                        if r+1 < len(grid) and grid[r+1][c] == "1": stack.append((r+1, c))
                        if c+1 < len(grid[0]) and grid[r][c+1] == "1": stack.append((r,c+1))
                        if r-1 >= 0 and grid[r-1][c] == "1": stack.append((r-1, c))
                        if c-1 >= 0 and grid[r][c-1] == "1": stack.append((r, c-1))
                    count += 1
        return count