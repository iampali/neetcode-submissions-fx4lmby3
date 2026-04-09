class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row, col = len(grid), len(grid[0])

        def bfs(r, c):
            grid[r][c] = "0"
            queue = [(r,c)]
            while queue:
                curr = queue.pop(0)
                directions = [(-1,0), (0, -1), (1, 0), (0, 1)] ## up, left, down, right
                for rd, cd in directions:
                    rd, cd = rd + curr[0] , cd + curr[1]
                    if (rd in range(row) and cd in range(col) and grid[rd][cd] == "1"):
                        queue.append((rd, cd))
                        grid[rd][cd] = "0"


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r,c)
                    count += 1
        

        return count
