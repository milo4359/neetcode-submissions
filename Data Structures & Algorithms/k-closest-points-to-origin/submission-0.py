class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        h = [(math.sqrt(x ** 2 + y ** 2), [x, y]) for [x, y] in points]
        heapq.heapify(h)
        while k > 0:
            d, [x, y] = heapq.heappop(h)
            res.append([x, y])
            k -= 1
        return res