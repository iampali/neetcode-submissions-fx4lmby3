class Solution:
    def isPalindrome(self, s, i, j):
        while(i < j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def helper(idx):
            if idx == len(s):
                res.append(part[:])
                return

            for j in range(idx, len(s)):
                if self.isPalindrome(s, idx, j):
                    part.append(s[idx : j + 1])
                    helper(j + 1)
                    part.pop()
        
        helper(0)

        return res