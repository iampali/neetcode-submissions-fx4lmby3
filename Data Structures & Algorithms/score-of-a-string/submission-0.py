class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        output = 0
        i = 1
        while i < n:
            output += abs( ord(s[i]) - ord(s[i-1]) )
            i += 1
        return output
