class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == n:
            return [[i for i in range(1, n+1)]]
        
        output = []
        def helper(curr, num):
            if len(curr) == k:
                output.append(curr[:])
                return
            
            for i in range(num, n+1):
                helper(curr + [i], i + 1)
                
            
        helper([],1)
        
        return output