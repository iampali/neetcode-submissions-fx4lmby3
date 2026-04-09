class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_K = float('-inf')
        def check_k(k):
            hours = 0
            for p in piles:
                hours += -(-p//k)
            return hours
        

        for p in piles:
            min_K = max(min_K, p)

        
        start ,end = 1 , min_K
        while(start <= end):
            mid = (start + end) // 2
            mid_min_hour = check_k(mid)
            if  h >= mid_min_hour : 
                min_K = mid
            
            if mid_min_hour > h:
                start = mid + 1
            else:
                end = mid - 1
            
        return min_K