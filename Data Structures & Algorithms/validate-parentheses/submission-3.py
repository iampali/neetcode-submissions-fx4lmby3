class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')' : '(',
            ']' :  '[',
            '}' :  '{'
        }

        stack = []

        if len(s) < 2:
            return False

        for i in s:
            if i in mapping:
                if not stack:
                    return False
                temp = stack.pop()
                if mapping[i] != temp:
                    return False
            else:
                stack.append(i)

        
        if stack:
            return False
        else:
            return True

        