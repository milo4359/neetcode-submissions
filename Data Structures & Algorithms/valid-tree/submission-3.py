class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        graph = defaultdict(list)
        visited = {0}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        q = deque([0])
        while q: 
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
            
        return len(visited) == n

        

