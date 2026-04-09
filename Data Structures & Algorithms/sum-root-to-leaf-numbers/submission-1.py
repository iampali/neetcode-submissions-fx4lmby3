# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root.right and not root.left:
            return root.val
        
        def helper(node, num):
            if not node:
                return 0
            
            num = num * 10 + node.val
            if not node.right and not node.left:
                return num
            
            left = helper(node.left, num)
            right = helper(node.right, num)
            return left + right

        
        return helper(root, 0)