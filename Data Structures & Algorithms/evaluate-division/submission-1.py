class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def bfs(source, target):
            if source not in graph or target not in graph:
                return -1
            
            queue = [(source, 1)]
            visited = set()
            visited.add(source)

            while queue:
                curr, w = queue.pop(0)
                if curr == target:
                    return w
                
                for neighbor, weight in graph[curr]:
                    if neighbor not in visited:
                        queue.append((neighbor, w * weight))
                        visited.add(neighbor)

            return -1



        return [bfs(source, target) for source,target in queries]