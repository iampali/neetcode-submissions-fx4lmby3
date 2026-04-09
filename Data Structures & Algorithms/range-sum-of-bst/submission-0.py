# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        sum = 0
        st = [root]
        if not root:
            return 0

        while(st):
            node = st.pop()
            if node.val >= low and node.val <= high:
                sum += node.val

            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)

        return sum 

        
        
