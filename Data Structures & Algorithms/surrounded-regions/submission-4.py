from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        corners = set([(r,0) for r in range(row)] + [(0,c) for c in range(col)] + [(row-1, c) for c in range(col)] + [(r, col-1) for r in range(row)])
        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))

            while queue:
                x, y = queue.popleft()
                if board[x][y] == "O":
                    board[x][y] = "T"

                for rd, cd in directions:
                    rd, cd = rd + x, cd + y
                    if rd in range(row) and cd in range(col) and board[rd][cd] == "O":
                        queue.append((rd,cd))


        print(corners)
        for i, j in corners:
            if board[i][j] == "O":
                bfs(i, j)


        for i in range(row):
            for j in range(col):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"