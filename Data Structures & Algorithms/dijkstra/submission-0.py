class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = collections.defaultdict(list)

        for i in edges:
            graph[i[0]].append((i[1], i[2]))

        print(graph)

        # compute shortest path
        shortest = {}
        queue = [(0, src)]
        while queue:
            w1, n1 = heapq.heappop(queue)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in graph[n1]:
                if n2 not in shortest:
                    heapq.heappush(queue, [w1 + w2, n2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
        
