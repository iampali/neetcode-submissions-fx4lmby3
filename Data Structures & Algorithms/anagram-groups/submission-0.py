class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        result = []
        for i in strs:
            a = str(sorted(i))
            if a in temp:
                temp[a].append(i)
            else:
                temp[a] = [i]

        for i in temp.values():
            result.append(i)
        return result

        