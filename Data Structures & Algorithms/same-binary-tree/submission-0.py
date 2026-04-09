# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        st1, st2 = [p], [q]

        while(st1 and st2):
            node1 = st1.pop()
            node2 = st2.pop()

            print(f"val of node1 is {node1.val} and node2 is {node2.val}")

            if node1.val != node2.val:
                return False

            if (node1.left and node2.left) or (not node1.left and not node2.left):
                if node1.left : st1.append(node1.left)
                if node2.left : st2.append(node2.left)
            else:
                return False
            
            if (node1.right and node2.right) or (not node1.right and not node2.right):
                if node1.right : st1.append(node1.right) 
                if node2.right : st2.append(node2.right)
            else:
                return False
        
        return True




        
        