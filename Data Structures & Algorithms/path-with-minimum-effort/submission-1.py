class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1, 0), (0 , -1)]

        row, col = len(heights), len(heights[0])
        target = (row - 1, col - 1)

        queue = [[0,(0,0)]]
        visited = set()

        while queue:
            w, curr = heapq.heappop(queue)
            if curr in visited:
                continue
            visited.add(curr)

            if curr == target:
                return w
            
            for rd,cd in directions:
                rd, cd = rd + curr[0], cd + curr[1]
                if rd >=0 and rd < row and cd >=0 and cd < col and (rd,cd) not in visited:
                    diff = max(w, abs(heights[rd][cd] - heights[curr[0]][curr[1]] ))
                    heapq.heappush(queue, [diff, (rd,cd)])