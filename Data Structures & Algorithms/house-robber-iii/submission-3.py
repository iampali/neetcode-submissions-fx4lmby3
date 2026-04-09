class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return (0,0)
            
            left = helper(node.left)
            right = helper(node.right)

            # with the node, if we want to include the node
            with_node = node.val + left[1] + right[1]

            # witout the root node, that means we can have hte maximised value from its children
            without_node = max(left) + max(right)

            return with_node, without_node
        
        result = helper(root)
        return max(result)
