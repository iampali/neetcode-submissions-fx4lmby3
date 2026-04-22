class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x : x*x)
        return [i*i for i in nums]