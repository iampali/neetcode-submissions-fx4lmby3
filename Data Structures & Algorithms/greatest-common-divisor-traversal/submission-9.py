from math import gcd
from collections import defaultdict, deque
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        graph = defaultdict(list)
        
        for i in range(n):
            for j in range(i+1, n):
                if gcd(nums[i], nums[j]) > 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        queue = deque([0])
        visit = {0}
        while queue:
            curr = queue.popleft()
            for nei in graph[curr]:
                if nei not in visit:
                    queue.append(nei)
                    visit.add(nei)

        return len(visit) == n
        
        
                