class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, skip)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we cannot rob children
            rob = node.val + left[1] + right[1]
            
            # If we skip this node, take best of children
            skip = max(left) + max(right)
            
            return (rob, skip)
        
        result = dfs(root)
        return max(result)
