class Solution:
    def solve(self, board: List[List[str]]) -> None:
        checked = set()
        rows, cols = len(board), len(board[0])
        q = deque()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in checked and board[r][c] == 'O':
                    change = True
                    region = set()
                    checked.add((r, c))
                    region.add((r, c))
                    q.append((r, c))
                    while q:
                        row, col = q.popleft()
                        for dr, dc in directions:
                            nr, nc = dr + row, dc + col
                            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and (nr, nc) not in checked:
                                q.append((nr, nc))
                                checked.add((nr, nc))
                                region.add((nr, nc))
                            elif not 0 <= nr < rows or not 0 <= nc < cols: change = False
                    if change:
                        for (row, col) in region: board[row][col] = 'X'
                        
