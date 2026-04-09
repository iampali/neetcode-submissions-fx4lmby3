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
        self.result = False
        def helper(node, sum_now):

            if not node:
                return
            
            if not node.left and not node.right:
                if sum_now + node.val == targetSum:
                    self.result = True
            
            helper(node.left, sum_now + node.val)
            helper(node.right, sum_now + node.val)
        
        helper(root, 0)
        return self.result


