class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = Counter(nums)
        for i in temp:
            if temp[i] >= len(nums) // 2:
                return i