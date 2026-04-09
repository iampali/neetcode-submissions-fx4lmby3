class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "empty" 
        return '\n'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        if s == 'empty':
            return []
        elif s == '':
            return [""]
        else:
            return s.split('\n')
