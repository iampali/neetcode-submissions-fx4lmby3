class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search_left_index(nums, target):
            start, end = 0, len(nums) - 1

            while(start <= end):
                mid = (start + end)//2
                if nums[mid] == target:
                    if mid == 0 : return 0
                    elif nums[mid - 1] == target:
                        end = mid - 1
                    else :
                        return mid
                elif target < nums[mid] : end = mid - 1
                else: start = mid + 1
            
            return -1

        def search_right_index(nums, target):
            start, end = 0, len(nums) - 1

            while(start <= end):
                mid = (start + end)//2
                if nums[mid] == target:
                    if mid == (len(nums) - 1) : return (len(nums) - 1)
                    elif nums[mid + 1] == target:
                        start = mid + 1
                    else :
                        return mid
                elif target < nums[mid] : end = mid - 1
                else: start = mid + 1
            
            return -1
        
        return [search_left_index(nums,target), search_right_index(nums,target)]