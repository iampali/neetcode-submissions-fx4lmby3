class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        n = len(s)
        if n%2 == 0:
            return( s[:n // 2] == s[n // 2:][::-1] )
        else:
            return( s[:n // 2] == s[(n + 1) // 2:][::-1] )


        