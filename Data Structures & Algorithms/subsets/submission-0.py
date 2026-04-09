class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]

        for i in nums:
            temp = [curr + [i] for curr in out]
            out.extend(temp)

        return out
