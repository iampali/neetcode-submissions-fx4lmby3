class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x
        
        ans = 1
        start, end = 0, x
        while(start < end):
            mid = (start + end) // 2
            print(f"start is {start}, end is {end} and mid is {mid}")

            if mid ** 2 <= x:
                ans = mid
                start = mid + 1
            else:
                end = mid

        return ans
                
        