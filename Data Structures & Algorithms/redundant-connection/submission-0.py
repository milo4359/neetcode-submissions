class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = list(range(len(edges) + 1))
        group = [1] * (len(edges) + 1)
        

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb: return [a, b]
            if group[pa] < group[pb]: pa, pb = pb, pa
            group[pa] += group[pb]
            parent[pb] = pa
        

                