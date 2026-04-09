class Solution:
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [i for i in count.values()]
        heapq.heapify_max(max_heap)
        q = deque()
        time = 0
        while q or max_heap:
            time += 1

            if max_heap:
                temp = heapq.heappop_max(max_heap)
                temp -= 1
                if temp:
                    q.append([temp, time + n])
            
            if q and q[0][1] == time:
                val = q.popleft()[0]
                heapq.heappush_max(max_heap, val)
        
        return time

