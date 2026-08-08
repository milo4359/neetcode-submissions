class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0

        pairs = sorted(zip(position, speed), reverse=True)
        head = -1
        for p, s in pairs:
            time = (target - p) / s
            if time > head:
                count += 1
                head = time
        
          

        return count
