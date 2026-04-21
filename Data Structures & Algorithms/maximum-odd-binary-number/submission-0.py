class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        no_of_1 = 0
        no_of_0 = 0

        for i in range(len(s)):
            if s[i] == '0':
                no_of_0 += 1
            else:
                no_of_1 += 1
        
        if not no_of_1 and no_of_0:
            return 0
        
        return f"{(no_of_1 - 1) * '1'}{no_of_0 * '0'}1"