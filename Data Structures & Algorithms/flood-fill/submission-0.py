class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])

        direction = [(1,0), (0,1), (0,-1), (-1,0)]
        start_color = image[sr][sc]

        if start_color == color:
            return image
        queue = [(sr, sc)]

        while queue:
            r, c = queue.pop(0)
            image[r][c] = color
    
            for rd, cd in direction:
                rd, cd = r + rd, c + cd
                if rd >=0 and rd < row and cd >=0 and cd < col and image[rd][cd] == start_color:
                    queue.append((rd,cd))
        
        return image