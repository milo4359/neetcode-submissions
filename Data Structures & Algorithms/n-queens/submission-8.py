class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        c, d1, d2 = set(), set(), set()
        res = []
        rows = []
        def dfs(row, col):
            if col == n: return
            if len(rows) == n:
                res.append(rows[:])
                return
            diagonal1 = n - 1 - row + col
            diagonal2 = row + col
            if col not in c and diagonal1 not in d1 and diagonal2 not in d2:
                c.add(col)
                d1.add(diagonal1)
                d2.add(diagonal2)
                rows.append('.' * col + 'Q' + '.' * (n - col - 1))
                dfs(row + 1, 0)
                c.discard(col)
                d1.discard(diagonal1)
                d2.discard(diagonal2)
                rows.pop()
            dfs(row, col + 1)
        
        dfs(0,0)
        return res
            
       
