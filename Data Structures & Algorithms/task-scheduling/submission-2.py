class Solution:
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = {}
        for i in tasks:
            h[i] = h.get(i, 0) + 1
        
        max_val, count = float("-inf"), 1

        for i in h:
            if h[i] > max_val:
                max_val = h[i]
                count = 1
            elif h[i] == max_val:
                count += 1

        parts = max_val - 1
        slots = parts * (n - (count - 1))
        rem_tasks = len(tasks) - (max_val * count)
        idle = slots - rem_tasks

        return (len(tasks) + max(0, idle))

