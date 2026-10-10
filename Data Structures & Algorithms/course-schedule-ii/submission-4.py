class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0: q.append(i)
        
        while q:
            course = q.popleft()
            res.append(course)
            for edge in graph[course]:
                indegree[edge] -= 1
                if indegree[edge] == 0: q.append(edge)
        
        return res if len(res) == numCourses else []
        

