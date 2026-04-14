from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (i,j), prob in zip(edges, succProb):
            graph[i].append((j, prob))
            graph[j].append((i, prob))

        output = -10**10

        queue = [(1.0, start_node)]
        visited = set()

        while queue:
            curr_prob, curr = heapq.heappop_max(queue)
            if curr == end_node:
                return curr_prob

            if curr in visited:
                continue
            visited.add(curr)
            
            for nei, nei_prob in graph[curr]:
                heapq.heappush_max(queue, (nei_prob * curr_prob, nei))


        if output == -10**10:
            return 0
        return output
