class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        row, col = len(grid), len(grid[0])

        def bfs(r, c):
            queue = [(r,c)]
            visited.add((r,c))
            while queue:
                curr = queue.pop(0)
                directions = [(-1,0), (0, -1), (1, 0), (0, 1)] ## up, left, down, right
                for rd, cd in directions:
                    rd, cd = rd + curr[0] , cd + curr[1]
                    if (rd in range(row) and cd in range(col) and (rd, cd) not in visited and grid[rd][cd] == "1"):
                        visited.add((rd, cd))
                        queue.append((rd, cd))


        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    count += 1
        

        return count
