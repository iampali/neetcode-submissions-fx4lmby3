class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited_global = []
        directions = [(1,0), (0,1), (-1,0), (0,-1)]


        row, col = len(grid), len(grid[0])

        def bfs(r,c):
            queue = [(r,c)]
            visited = set()
            visited.add((r,c))
            while queue:
                r, c = queue.pop(0)
                grid[r][c] = 0
                for rd,cd in directions:
                    rd, cd = r + rd, c + cd
                    if rd >= 0 and rd < row and cd >= 0 and cd < col and grid[rd][cd] == 1 and (rd, cd) not in visited:
                        queue.append((rd,cd))
                        visited.add((rd,cd))
            
            return visited


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    visited_global.append(bfs(i,j))

        res = float('inf')

        for ra, ca in visited_global[0]:
            for rb, cb in visited_global[1]:
                diff = abs(ra - rb) + abs(ca - cb) - 1
                res = min(res, diff)
        
        return res
                

