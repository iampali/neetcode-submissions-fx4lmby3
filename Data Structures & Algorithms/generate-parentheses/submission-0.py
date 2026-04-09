class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(curr, open_count, close_count):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            if open_count < n:
                helper(curr + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                helper(curr + ')', open_count, close_count + 1)
        
        helper("", 0, 0)
        return res
            
