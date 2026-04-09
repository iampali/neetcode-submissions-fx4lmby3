# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        res = []

        def helper(node, level):
            if len(res) == level:
                res.append([])
            val = node.val if node else None
            res[level].append(val)
            if not node:
                return
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root,0)
        print(res)
        flag = False
        for i in res:
            for j in i:
                if j is None:
                    flag = True
                if j is not None and flag:
                    return False
        return True
        

        
            
            

        