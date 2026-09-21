class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-x for x in nums]
        heapq.heapify(h)
        for i in range(k - 1):
            heapq.heappop(h)
        return -h[0]