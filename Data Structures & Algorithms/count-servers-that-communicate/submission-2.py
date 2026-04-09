class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        
        connections = 0

        def bfs(r,c):
            conn = 0
            queue = [(r,c)]
            grid[r][c] = 2
            while queue:
                r,c = queue.pop(0)
                conn += 1

                for i in range(row):
                    if grid[i][c] == 1:
                        queue.append((i,c))
                        grid[i][c] = 2

                
                for i in range(col):
                    if grid[r][i] == 1:
                        queue.append((r,i))
                        grid[r][i] = 2
                        
            
            return conn if conn != 1 else 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    connections += bfs(i,j)
        
        return connections
            



