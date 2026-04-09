import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k+1):

            temp_array = prices.copy()

            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                
                if prices[s] + p < temp_array[d]:
                    temp_array[d] = prices[s] + p

            prices = temp_array
        
        return -1 if prices[dst] == float('inf') else prices[dst]
