
from math import gcd
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if 1 in nums:
            return False
        nums=sorted(set(nums),reverse=True) # sord in dec order
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):  
            # if gcd of 2 number is
            # 1 then gcd(nums[i],nums[j])-1 will bcome zero and the 
            # condition will not be executed
                if gcd(nums[i],nums[j])-1:  # check if the gcd of 2 numbers exist
                    nums[j]*=nums[i]
                    break
            else:
                return False    # no potential match
        return True