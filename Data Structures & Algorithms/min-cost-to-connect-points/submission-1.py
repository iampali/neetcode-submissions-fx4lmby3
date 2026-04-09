class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        src = points[0]
        queue = [ [0, src[0], src[1]] ]
        visited = set()
        cost = 0

        while queue:
            w, i, j = heapq.heappop(queue)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            cost += w
            print(f"Running for {i, j , w}")
            
            for r, c in points:
                if (i,j) != (r,c) and (r,c) not in visited:
                    diff = abs(i - r) + abs(j - c)
                    print(f"pusing {r,c, diff}")
                    heapq.heappush(queue, [diff, r , c])
        
        return cost


