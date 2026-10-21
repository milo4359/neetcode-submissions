class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        time = [float('inf')] * (n+1)
        time[0] = -1
        time[k] = 0

        q = deque([(k, 0)])
        while q:
            u, tcurr = q.popleft()
            for v, t in graph[u]:
                tv = t + tcurr
                if tv < time[v]:
                    q.append((v, tv))
                    time[v] = tv

        minimum = max(time)
        return -1 if minimum == float('inf') else minimum
