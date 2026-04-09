from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        row, col = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < row and 0 <= nc < col and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return visited

        # 🌊 Pacific (top row + left col)
        pacific_starts = [(0, c) for c in range(col)] + [(r, 0) for r in range(row)]
        print(pacific_starts)

        # 🌊 Atlantic (bottom row + right col)
        atlantic_starts = [(row - 1, c) for c in range(col)] + [(r, col - 1) for r in range(row)]
        print(atlantic_starts)

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return list(pacific & atlantic)