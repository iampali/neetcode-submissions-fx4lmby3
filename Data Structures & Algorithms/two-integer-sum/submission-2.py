class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        temp = {}

        for i in range(n):
            required = target - nums[i]
            if required in temp:
                return [temp[required], i]
            else:
                temp[nums[i]] = i

        

        