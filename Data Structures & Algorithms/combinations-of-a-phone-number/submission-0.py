class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        if not digits:
            return output
        
        mapping = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def helper(idx, curr):
            if idx == len(digits):
                output.append(curr)
                return
            
            for option in mapping[digits[idx]]:
                helper(idx + 1, curr + option)
        
        helper(0, "")
        return output



