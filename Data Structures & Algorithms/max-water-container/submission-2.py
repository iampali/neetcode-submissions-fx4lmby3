class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_result = float('-inf')
        while(i < j):
            result = (j - i)*( min(heights[i], heights[j]) )
            max_result =  max( result , max_result)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return max_result


        