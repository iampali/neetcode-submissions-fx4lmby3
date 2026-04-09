class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        for i, _ in zip(range(len(word1)), range(len(word2))):
            out += word1[i] + word2[i]
        
        out += word1[i+1:] + word2[i+1:]

        return out