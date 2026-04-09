class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == n:
            return [[i for i in range(1, n+1)]]
        
        output = []
        def helper(index, curr):
            if len(curr) == k:
                output.append(curr[:])
                return
            
            need = k - len(curr)
            for j in range(index, n-(need-1)+1):
                curr.append(j)
                helper(j+1, curr)
                curr.pop()
            
        helper(1, [])
        
        return output