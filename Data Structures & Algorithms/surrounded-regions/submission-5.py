from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(r, c):
            queue = deque([(r, c)])
            board[r][c] = "T"

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == "O":
                        board[nx][ny] = "T"
                        queue.append((nx, ny))

        # Traverse borders directly (no set needed)
        for i in range(row):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for j in range(col):
            if board[0][j] == "O":
                bfs(0, j)
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        # Final transformation
        for i in range(row):
            for j in range(col):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"