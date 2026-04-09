class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for i, j, m in flights:
            graph[i].append((j, m))
        
        print(graph)
        queue = [(0, src, k+1)]
        visited = set()
        while queue:
            w, curr, curr_k = heapq.heappop(queue)

            print(f"Curr is {curr} and k is {curr_k}")

            
            if curr_k >= 0 and curr == dst:
                return w
            
            for neighbor, price in graph[curr]:
                if curr_k >= 1:
                    heapq.heappush(queue, (w + price, neighbor, curr_k - 1))
        
        return -1

