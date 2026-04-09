"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}

        def helper(node):
            if not node:
                return None
            
            if node.val in visited:
                return visited[node.val]

            curr = Node(node.val)
            visited[curr.val] = curr

            for neighbor in node.neighbors:
                temp = helper(neighbor)
                if temp:
                    curr.neighbors.append(temp)

            return curr

        return helper(node)