from math import sqrt, floor
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        while k:
            curr = heapq.heappop_max(gifts)

            curr = floor(sqrt(curr))

            heapq.heappush_max(gifts, curr)

            k -= 1
        

        return sum(list(gifts))