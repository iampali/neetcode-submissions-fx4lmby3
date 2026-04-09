class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def helper(curr, idx, curr_sum):
            if curr_sum == target:
                output.append(curr[:])
                return
            
            if curr_sum > target:
                return
            
            for i in range(idx, len(nums)):
                helper(curr + [nums[i]], i, curr_sum + nums[i])  # stay at i
        
        helper([],0, 0)

        return output