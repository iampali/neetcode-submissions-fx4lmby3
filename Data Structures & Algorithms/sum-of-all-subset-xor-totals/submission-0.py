class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.output = 0

        def helper(idx, curr, curr_xor):
            if idx == len(nums):
                self.output += curr_xor
                return
            
            helper(idx + 1, curr, curr_xor)
            helper(idx + 1 , curr + [nums[idx]], curr_xor ^ nums[idx])
        
        helper(0,[],0)

        return self.output
