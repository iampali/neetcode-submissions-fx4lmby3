class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_left, max_right = height[i], height[j]
        result = 0
        while(i < j):
            if height[j] < height[i]:
                result += max(max_right - height[j], 0)
                max_right = max(max_right, height[j])
                j -= 1
            else:
                result += max(max_left - height[i], 0)
                max_left = max(max_left, height[i])
                i += 1
        
        return result
        