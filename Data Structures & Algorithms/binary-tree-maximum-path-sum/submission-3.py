# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        if not root:
            return res
        if not root.left and not root.right:
            return root.val

        def helper(node):
            if not node:
                return float('-inf')
            
            left = helper(node.left)
            right = helper(node.right) 
            print(f"At node {node.val}")
            print(f"left is {left}")
            print(f"right is {right}")
            max_child = max(left, right)
            max_now = max( node.val, max( node.val + max_child, node.val + left + right))            
            
            self.res = max(self.res, max_now)
            print(f"value of max_now is {max_now}")

            print(f"value of self.res is {self.res}")

            return max(node.val + max_child, node.val)


        helper(root)
        return self.res
