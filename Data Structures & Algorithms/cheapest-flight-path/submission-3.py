import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        # Construct the graph: each node (airport) has a list of (neighbor, price)
        for i, j, m in flights:
            graph[i].append((j, m))

        # Min-heap priority queue (cost, current node, remaining stops)
        queue = [(0, src, k+1)]  # Start with src, 0 cost, and k+1 stops
        visited = {}

        while queue:
            cost, curr, stops_left = heapq.heappop(queue)

            # If we have reached the destination, return the cost
            if curr == dst:
                return cost

            # Avoid processing a node with fewer remaining stops if it's already been visited
            if (curr, stops_left) in visited:
                continue

            visited[(curr, stops_left)] = cost

            # If there are stops left, process the neighbors
            if stops_left > 0:
                for neighbor, price in graph[curr]:
                    heapq.heappush(queue, (cost + price, neighbor, stops_left - 1))

        # If no path is found, return -1
        return -1