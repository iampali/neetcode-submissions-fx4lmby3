class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        res = 0

        def bfs(r,c):
            queue = [(r,c)]
            local_visited = set()
            local_visited.add((r,c))
            flag = False
            while queue:
                r,c = queue.pop(0)
                if r == 0 or r == row-1 or c == 0 or c == col-1:
                    flag = True
                
                grid[r][c] = 0

                for rd,cd in directions:
                    rd, cd = r + rd, c + cd
                    if rd >=0 and rd < row and cd >= 0 and cd < col and grid[rd][cd] == 1 and (rd,cd) not in local_visited:
                        queue.append((rd,cd))
                        local_visited.add((rd,cd))
                
            return len(local_visited) if not flag else 0


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res += bfs(i,j)

        return res