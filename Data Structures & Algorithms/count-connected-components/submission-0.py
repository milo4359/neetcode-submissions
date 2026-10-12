class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)
        count = 0
        q = deque()
        for i in range(n):
            if i not in visited:
                q.append(i)
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                count += 1
        return count
