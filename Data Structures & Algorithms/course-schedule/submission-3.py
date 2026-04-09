from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        for i in prerequisites:
            graph[i[1]].append(i[0])
        
        for vertex in range(numCourses):

            queue = deque()
            visited = {}
            for i in range(len(graph[vertex])):
                queue.append(graph[vertex][i])
            while queue:
                curr = queue.popleft()
                visited[curr] = True
                if curr == vertex:
                    return False
                neighbours = graph[curr]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)
        
        return True