# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root : return root
        def helper(curr):
            temp = curr.right
            curr.right = curr.left
            curr.left = temp

            if curr.left: helper(curr.left)
            if curr.right: helper(curr.right)

            return curr

        return helper(root)
            

        