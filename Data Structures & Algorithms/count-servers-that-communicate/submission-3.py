class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        row_cnt = [0] * row
        col_cnt = [0] * col

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        print(row_cnt, col_cnt) 
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] and max(row_cnt[r], col_cnt[c]) > 1:
                    res += 1
        return res

