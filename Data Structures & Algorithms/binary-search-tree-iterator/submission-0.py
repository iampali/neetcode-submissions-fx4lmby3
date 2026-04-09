# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []

        def helper(node):
            if node.left : helper(node.left)
            self.res.append(node.val)
            if node.right : helper(node.right)
        

        helper(root)

        self.pointer = None
        self.index = -1
        

    def next(self) -> int:
        self.index += 1
        self.pointer = self.res[self.index]
        return self.pointer

    def hasNext(self) -> bool:
        if self.index != len(self.res) - 1:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()