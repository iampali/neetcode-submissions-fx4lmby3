class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        start = '0000'

        if start in deadends:
            return -1
        queue = [(start,0)]
        visited = set()
        visited.add(start)
        visited.update(deadends)
        ans = 0

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        while queue:
            curr, step = queue.pop(0)
            if curr == target:
                return step
            for neighbor in children(curr):
                if neighbor not in visited:
                    queue.append((neighbor,step+1))
                    visited.add(neighbor)
        
        return -1