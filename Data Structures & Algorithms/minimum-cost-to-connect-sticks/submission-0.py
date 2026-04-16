class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        output = 0
        if len(sticks) == 1:
            return output
        
        heapq.heapify(sticks)

        while len(sticks) != 1:
            curr = heapq.heappop(sticks)
            curr2 = heapq.heappop(sticks)

            output += curr + curr2

            heapq.heappush(sticks, curr + curr2)
        
        return output

