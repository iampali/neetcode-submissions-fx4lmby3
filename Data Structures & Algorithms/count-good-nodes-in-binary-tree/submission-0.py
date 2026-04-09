# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return self.ans
        
        if not root.left and not root.right:
            return self.ans + 1
        
        def helper(node, root):
            if node.val >= root.val:
                self.ans += 1
            
            if node.left : helper(node.left, max(root, node, key= lambda x : x.val))
            if node.right : helper(node.right, max(root, node, key= lambda x : x.val))

            
        helper(root, root)
        return self.ans



