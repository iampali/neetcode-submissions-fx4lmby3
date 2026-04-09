class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        results = []
        for i, a in enumerate(arr):
            if i > 0 and a == arr[i-1]:
                continue
            
            j, k = i+1, len(arr) - 1

            while(j < k):
                num_sum = a + arr[j] + arr[k]
                if num_sum > 0:
                    k -= 1
                elif num_sum < 0:
                    j += 1
                else:
                    results.append([a, arr[j], arr[k]])
                    j += 1
                    while(arr[j] == arr[j - 1] and j < k):
                        j += 1
        
        return results

