class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        max_length = 1
        n = len(s)
        if n == 0: return 0
        if n == 1: return max_length

        while(j < n+1):
            if (j - i) == len(set(s[i:j])):
                max_length = max((j - i), max_length)
                j += 1
            else:
                i += 1
        
        return max_length
        