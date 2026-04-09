import math
from collections import defaultdict

class Solution:
    def canTraverseAllPairs(self, nums):
        if len(nums) == 1:
            return True
        
        if 1 in nums:
            return False
        
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Initialize parent
        for num in nums:
            parent[num] = num
        
        factor_map = {}  # factor -> first number seen
        
        def get_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors
        
        for num in nums:
            factors = get_factors(num)
            for f in factors:
                if f in factor_map:
                    union(num, factor_map[f])
                factor_map[f] = num
        
        root = find(nums[0])
        return all(find(num) == root for num in nums)