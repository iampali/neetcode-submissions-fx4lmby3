# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        
        val = 0
        left1, left2, right1, right2 = None,None,None,None

        if root1 and root2:
            val = root1.val + root2.val
            left1 = root1.left
            right1 = root1.right
            left2 = root2.left
            right2 = root2.right
        elif root1:
            val = root1.val
            left1 = root1.left
            right1 = root1.right
        elif root2:
            val = root2.val
            left2 = root2.left
            right2 = root2.right

        root = TreeNode(val)


        root.left = self.mergeTrees(left1, left2)
        root.right = self.mergeTrees(right1, right2)

        return root
        





