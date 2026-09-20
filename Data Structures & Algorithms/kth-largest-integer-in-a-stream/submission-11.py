class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        start = max(0, len(nums) - k)
        self.k = k
        ordered = sorted(nums)
        self.h = ordered[start:]
        heapq.heapify(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < 1 or val > (self.h[0]):
            if (len(self.h) < self.k): heapq.heappush(self.h, val)
            else: heapq.heapreplace(self.h, val)
        return self.h[0]

        
