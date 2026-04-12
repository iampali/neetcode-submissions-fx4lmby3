class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        
        for curr in strs:
            if curr == "":
                return ""
            if res != curr:
                j = 0
                while j < min(len(res), len(curr)):
                    if res[j] != curr[j]:
                        break
                    j += 1
            
                res = res[:j]
        
        return res
            


