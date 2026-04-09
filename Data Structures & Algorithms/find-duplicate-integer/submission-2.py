class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            i = abs(i)
            if nums[i] < 0:
                return i
            nums[i] *= -1