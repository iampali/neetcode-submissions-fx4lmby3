class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        visited = set()

        queue = [(grid[0][0],0,0)]

        while queue:
            t , r, c = heapq.heappop(queue)
            if (r,c) in visited:
                continue

            visited.add((r,c))
            if (r,c) == (n-1, n-1):
                return t
            
            for rd,cd in directions:
                rd,cd = rd +r , cd + c

                if rd>=0 and rd < n and cd >=0 and cd < n and (rd,cd) not in visited:
                    heapq.heappush(queue, (max(t, grid[rd][cd]), rd, cd))            
    