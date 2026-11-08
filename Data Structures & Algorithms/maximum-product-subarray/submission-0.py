class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        subs = []
        cur = []
        res = float('-inf')

        for num in nums:
            res = max(res, num)
            if num == 0:
                if cur:
                    subs.append(cur)
                    cur = []
            else:
                cur.append(num)
            
        if cur: subs.append(cur)

        for sub in subs:
            if len(sub) == 1:
                res = max(res, sub[0])
                continue
            neg = 0
            prod = 1
            for num in sub:
                prod *= num
                if num < 0:
                    neg += 1
            if neg % 2 == 0: res = max(res, prod)
            else:
                i, j = 0, len(sub) - 1
                prodi, prodj = 1, 1
                while sub[i] > 0 or sub[j] > 0:
                    if sub[i] > 0: 
                        prodi *= sub[i]
                        i += 1
                    if sub[j] > 0: 
                        prodj *= sub[j]
                        j -= 1
                prodi, prodj = prodi * sub[i], prodj * sub[j]
                res = max(res, prod // prodi, prod // prodj)
        return res



