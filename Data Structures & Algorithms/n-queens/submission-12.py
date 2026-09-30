class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        c, d1, d2 = set(), set(), set()
        res = []
        rows = []
        def dfs(row):
            if len(rows) == n:
                res.append(rows[:])
                return
            
            for col in range(n):
                diagonal1 = row - col
                diagonal2 = row + col
                if col not in c and diagonal1 not in d1 and diagonal2 not in d2:
                    c.add(col)
                    d1.add(diagonal1)
                    d2.add(diagonal2)
                    rows.append('.' * col + 'Q' + '.' * (n - col - 1))
                    dfs(row + 1)
                    c.discard(col)
                    d1.discard(diagonal1)
                    d2.discard(diagonal2)
                    rows.pop()
        
        dfs(0)
        return res
            
       
