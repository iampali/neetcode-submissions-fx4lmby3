class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 1
        has_zero = False
        zero_count = 0
        for i in nums:
            if i == 0:
                has_zero = True
                zero_count += 1
            
            if i != 0:
                count *= i
        
        if has_zero and zero_count > 1:
            return [0 for _ in nums]
        
        elif not has_zero:
            return [count//i for i in nums]
        else:
            return [0 if i != 0 else count for i in nums]
 
            
        
