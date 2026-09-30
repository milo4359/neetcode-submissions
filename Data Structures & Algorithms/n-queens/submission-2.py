class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r, c, d1, d2 = defaultdict(bool), defaultdict(bool), defaultdict(bool), defaultdict(bool)
        res = []
        rows = []
        def dfs(row, col):
            if col == n: return
            if len(rows) == n:
                res.append(rows[:])
                return
            diagonal1 = n - 1 - row + col
            diagonal2 = row + col
            if not r.get(row) and not c.get(col) and not d1.get(diagonal1) and not d2.get(diagonal2):
                r[row] = True
                c[col] = True
                d1[diagonal1] = True
                d2[diagonal2] = True
                rows.append('.' * col + 'Q' + '.' * (n - col - 1))
                dfs(row + 1, 0)
                r[row] = False
                c[col] = False
                d1[diagonal1] = False
                d2[diagonal2] = False
                rows.pop()
            dfs(row, col + 1)
        
        dfs(0,0)
        return res
            
       
