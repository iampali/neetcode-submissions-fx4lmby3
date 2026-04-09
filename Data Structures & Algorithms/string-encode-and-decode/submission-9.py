class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "#####" 
        return '\n'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        if s == '#####':
            return []
        elif s == '':
            return [""]
        else:
            return s.split('\n')
