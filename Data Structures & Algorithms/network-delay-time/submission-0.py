class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        result = 0
        visited = set()

        graph = collections.defaultdict(list)

        for i,j,m in times:
            graph[i].append((j,m))

        queue = [(0, k)]

        while queue:
            w1, n1 = heapq.heappop(queue)

            if n1 in visited:
                continue
            visited.add(n1)
            result = max(w1, result)

            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(queue, (w1 + w2, n2))

        if n == len(visited):
            return result
        else:
            return -1