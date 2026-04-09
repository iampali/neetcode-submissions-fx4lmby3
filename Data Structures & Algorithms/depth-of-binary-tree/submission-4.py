# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        if not root : return self.maximum
        if not root.left and not root.right : return 1

        def helper(curr, depth_now):
            if not curr.left and not curr.right:
                self.maximum = max(self.maximum, depth_now)

            if curr.left : helper(curr.left, depth_now + 1)            
            if curr.right : helper(curr.right, depth_now + 1)

        helper(root, 1)        
        return self.maximum



        