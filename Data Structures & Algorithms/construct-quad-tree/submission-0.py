"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def check_values(self, grid):
        if sum([sum(b) for b in grid]) == 0:
            return 0
        elif sum([sum(b) for b in grid]) == (len(grid) * len(grid[0])):
            return 1
        else:
            return -1

    def construct(self, grid: List[List[int]]) -> 'Node':
        check = self.check_values(grid)
        root = Node(check, isLeaf=1)
        if check == 0 or check == 1:
            return root
        
        root.isLeaf = 0
        m, n = len(grid), len(grid[0])
        top_left = [ i[:n//2] for i in grid[:m//2] ]
        top_right = [ i[n//2:] for i in grid[:m//2] ]
        bottom_left = [ i[:n//2] for i in grid[m//2:] ]
        bottom_right = [ i[n//2:] for i in grid[m//2:] ]

        root.topLeft = self.construct(top_left)
        root.topRight = self.construct(top_right)
        root.bottomLeft = self.construct(bottom_left)
        root.bottomRight = self.construct(bottom_right)

        return root

        



        