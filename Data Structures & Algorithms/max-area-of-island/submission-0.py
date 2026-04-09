class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        if not grid:
            return ans

        directions = [(1,0), (0,1), (-1,0), (0, -1)]

        row, col = len(grid), len(grid[0])

        def bfs(r,c):
            count = 0
            queue = [(r,c)]
            grid[r][c] = 0

            while queue:
                curr = queue.pop(0)
                count += 1
                for rd, cd in directions:
                    rd, cd = rd + curr[0], cd + curr[1]
                    if rd in range(row) and cd in range(col) and grid[rd][cd] == 1:
                        queue.append((rd,cd))
                        grid[rd][cd] = 0
            
            return count

            

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans = max( ans, bfs(i,j))
        
        return ans