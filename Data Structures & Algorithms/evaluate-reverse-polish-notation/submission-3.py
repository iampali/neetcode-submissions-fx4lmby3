class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operations = {
            '+' : lambda a,b : a + b,
            '-' : lambda a,b : a - b,
            '*' : lambda a,b : a * b,
            '/' : lambda a,b : int(a / b)
        }
        stack = []
        for i in tokens:
            if i in valid_operations:
                b = int(stack.pop())
                a = int(stack.pop())

                out = valid_operations[i](a , b)

                stack.append(out)
            else:
                stack.append(int(i))

        return stack.pop()
