class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(arr)):
            need = set()
            for j in range(i+1,len(arr)):
                value_needed = -(arr[i] + arr[j])
                if value_needed in need:
                    triplet = tuple(sorted((arr[i], arr[j], value_needed)))
                    res.add(triplet)
                need.add(arr[j])
        return [list(triplet) for triplet in res]
