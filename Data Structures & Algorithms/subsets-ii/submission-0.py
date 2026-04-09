class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums.sort()

        def helper(subset, idx):
            if idx == len(nums):
                output.append(subset[:])
                return
            
            # include

            subset.append(nums[idx])
            helper(subset, idx + 1)
            subset.pop()


            # exclude
            while idx < len(nums) - 1 and nums[idx] == nums[idx+1]:
                idx += 1
            
            helper(subset, idx + 1)
        
        helper([], 0)
        return output