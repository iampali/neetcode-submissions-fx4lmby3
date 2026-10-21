class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        output = 0
        while j > i:
            water = min(heights[i], heights[j]) * (j - i)
            print(water)
            output = max(output, water)
            if heights[i] > heights[j] :
                j -= 1
            else:
                i += 1
        
        return output


        