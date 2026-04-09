from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue = deque([(r,c)])
                    visited.add((r,c))
                    perimeter = 0

                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                                perimeter += 1
                            elif grid[nx][ny] == 0:
                                perimeter += 1
                            elif (nx,ny) not in visited:
                                visited.add((nx,ny))
                                queue.append((nx,ny))

                    return perimeter