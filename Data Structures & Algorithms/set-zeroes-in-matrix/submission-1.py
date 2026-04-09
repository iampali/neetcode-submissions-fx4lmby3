class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])

        visited = set()

        def change(r,c):
            for i in range(row):
                if matrix[i][c] != 0:
                    matrix[i][c] = 0
                    visited.add((i,c))
            
            for j in range(col):
                if matrix[r][j] != 0:
                    matrix[r][j] = 0
                    visited.add((r,j))


        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and matrix[r][c] == 0:
                    change(r,c)
