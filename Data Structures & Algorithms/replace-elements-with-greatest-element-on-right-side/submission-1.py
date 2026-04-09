class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        n = len(arr)
        for i in range(n - 1, -1, -1):
            # Keep track of value to calculate maximum because we overwrite it
            value = arr[i]
            arr[i] = rightMax

            rightMax = max(value, rightMax)

        return arr
        