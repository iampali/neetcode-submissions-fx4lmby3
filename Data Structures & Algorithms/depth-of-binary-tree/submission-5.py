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
            if not curr : return 0
            if not curr.left and not curr.right:
                return depth_now

            left_height = helper(curr.left, depth_now + 1)            
            right_height = helper(curr.right, depth_now + 1)

            return max(left_height, right_height)

        return helper(root, 1)



        