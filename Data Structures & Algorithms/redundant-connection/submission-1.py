from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = {}

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            indegree[i] = indegree.get(i, 0) + 1
            indegree[j] = indegree.get(j, 0) + 1

        stack = []

        for i in indegree:
            if indegree[i] == 1:
                stack.append(i)

        while stack:
            curr = stack.pop()
            indegree[curr] -= 1
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    stack.append(neighbor)

        

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []
        