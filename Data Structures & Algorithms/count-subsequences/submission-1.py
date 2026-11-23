class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        used = defaultdict(int)
        used[0] = 1

        for c in s:
            for i in sorted(used, reverse=True):
                if i < len(t) and t[i] == c:
                    used[i+1] += used[i]

        return used[len(t)] 