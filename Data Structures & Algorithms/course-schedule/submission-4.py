from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1

        print(graph)
        print(indegree)

        count = 0
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        while stack:
            curr = stack.pop()
            count += 1

            for neighbour in graph[curr]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    stack.append(neighbour)
            

        return count == numCourses      
        
        