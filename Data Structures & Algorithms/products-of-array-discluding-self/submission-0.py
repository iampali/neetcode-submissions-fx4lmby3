class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        prod = 1
        for i in nums:
            if i == 0 :
                count += 1
            else:
                prod *= i
        
        if count == 0:
            return [prod // i for i in nums]
        elif count == 1:
            return [0 if i != 0 else prod for i in nums]
        else:
            return [0 for _ in nums]


        
        return results
        