class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
            
        row, col = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1),(-1,-1), (1,1), (-1,1), (1,-1)]
        tgt = (row-1, col-1)
        queue = [(1,0,0)]
        visited = set()
        visited.add((0,0))
        ans = 1

        while queue:
            curr_ans, r,c = heapq.heappop(queue)
            if (r,c) == tgt:
                return curr_ans

            for rd,cd in directions:
                rd,cd = rd +r , cd + c
                if rd >= 0 and rd < row and cd >= 0 and cd < col and grid[rd][cd] == 0 and (rd,cd) not in visited:
                    heapq.heappush(queue, (curr_ans + 1, rd, cd))
                    visited.add((rd,cd))
        
        return -1

