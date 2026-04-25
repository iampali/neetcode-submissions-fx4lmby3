class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        d = collections.deque()

        for i in nums:
            if i % 2 :
                d.append(i)
            else:
                d.appendleft(i)
        
        return list(d)

            