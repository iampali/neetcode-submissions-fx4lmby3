"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        res = []
        if not root:
            return root
        
        def helper(node, level):
            if not node:
                return None
            
            if len(res) == level:
                res.append([])
            
            res[level].append(node)
            
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        helper(root, 0)
        output = []
        for i in res:
            for j in range(len(i)):
                if j != len(i)-1:
                    i[j].next = i[j+1]
                else:
                    i[j].next = None


        return root
            
            
        