# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def helper(node, sum_now):

            if not node:
                return False
            
            if not node.left and not node.right:
                return ((sum_now + node.val) == targetSum)
            
            return helper(node.left, sum_now + node.val) or helper(node.right, sum_now + node.val)
        
        return helper(root, 0)