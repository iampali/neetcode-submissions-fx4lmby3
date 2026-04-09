from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False] * len(queries)
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for i, j in prerequisites:
            graph[i].append(j)
            indegree[j] += 1
        
        stack = []
        isPrereq = [set() for _ in range(numCourses)]


        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                isPrereq[neighbor].add(node)
                isPrereq[neighbor].update(isPrereq[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)

        return [u in isPrereq[v] for u, v in queries]