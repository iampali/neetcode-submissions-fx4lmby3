class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited_global = set()

        def bfs(r,c):
            queue = [(r,c)]
            visited = set()
            visited.add((r,c))

            while queue:
                x, y = queue.pop(0)
                if x == 0 or x == row-1 or y == 0 or y == col-1:
                    visited_global.update(visited)
                    return
                for rd, cd in directions:
                    rd, cd = rd + x, cd + y

                    if rd in range(row) and cd in range(col) and board[rd][cd] == "O" and (rd,cd) not in visited:
                        queue.append((rd,cd))
                        visited.add((rd,cd))

            
            for x, y in visited:
                board[x][y] = "X"
                visited_global.update(visited)


        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i,j) not in visited_global:
                    bfs(i, j)