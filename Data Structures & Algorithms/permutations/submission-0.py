class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []


        def helper(curr):
            if len(curr) == len(nums):
                output.append(curr[:])
                return
            
            for j in nums:
                if j not in curr:
                    helper(curr + [j])

        helper([])
        return output