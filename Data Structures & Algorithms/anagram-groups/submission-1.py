class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for i in strs:
            a = str(sorted(i))
            if a in temp:
                temp[a].append(i)
            else:
                temp[a] = [i]

        return list(temp.values())

        