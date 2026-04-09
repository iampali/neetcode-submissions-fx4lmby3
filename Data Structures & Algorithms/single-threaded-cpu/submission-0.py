class Solution:
    from collections import deque
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []
        for i, (enqueueTime, processingTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processingTime, i))

        time = 0
        res = []
        while pending or available:
            while pending and pending[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processTime, i))
            
            if not available:
                time = pending[0][0]
                continue
            
            processTime, i = heapq.heappop(available)
            time += processTime
            res.append(i)

        return res
