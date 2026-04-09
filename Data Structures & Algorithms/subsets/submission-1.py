class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def helper(subset, idx):
            if idx == len(nums):
                out.append(subset[:])
                return
            
            helper(subset, idx + 1)
            helper(subset + [nums[idx]], idx + 1)
        

        helper([], 0)
        return out


