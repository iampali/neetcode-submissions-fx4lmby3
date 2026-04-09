class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temps = {}
        for i in nums:
            temps[i] = temps.get(i, 0) + 1
        temps = sorted(temps, key = lambda x : temps[x], reverse=True)

        return temps[:k]
        