from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        

        output = []
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)

        while stack:
            curr = stack.pop()
            output.append(curr)

            for neighbour in graph[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    stack.append(neighbour)

        return output if len(output) == numCourses else []