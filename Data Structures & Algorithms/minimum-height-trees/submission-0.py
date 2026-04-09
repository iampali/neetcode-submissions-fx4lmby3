class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        

        def dfs(i):
            queue = [(i, 1)]
            visited = set()
            visited.add(i)
            max_level = 0
            while queue:
                curr, level = queue.pop(0)
                max_level = max(max_level, level)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        queue.append((neighbor, level + 1))
                        visited.add(neighbor)
            
            return max_level

        heights = collections.defaultdict(list)
        for i in range(n):
            height = dfs(i)
            heights[height].append(i)

        output = min(heights)


        return heights[output]