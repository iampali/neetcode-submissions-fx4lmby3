class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row, col = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(r,c):
            queue = [(r,c)]
            visited = set()
            while queue:
                curr = queue.pop(0)
                temp = grid[curr[0]][curr[1]]
                for rd, cd in directions:
                    rd ,cd = rd + curr[0] , cd + curr[1]
                    if rd in range(row) and cd in range(col) and grid[rd][cd] != 0 and grid[rd][cd] != -1 and (rd,cd) not in visited :
                        grid[rd][cd] = min(grid[rd][cd], temp + 1)
                        visited.add((rd,cd))
                        queue.append((rd,cd))


            

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    bfs(i,j)

