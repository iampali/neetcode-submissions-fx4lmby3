class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        k = len(positions)
        output = [0] * k
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        land_positions = set()

        for index, (r,c) in enumerate(positions):
            if (r,c) in land_positions:
                res = output[index - 1]

            else:
                land_positions.add((r,c))
                if index == 0:
                    output[index] = 1
                    continue
                
                curr_island = output[index - 1]
                count = 0
                for rd,cd in directions:
                    rd, cd = rd + r, cd + c
                    if rd >= 0 and rd < m and cd >= 0 and cd < n and (rd,cd) in land_positions:
                        count += 1
                
                res = curr_island - count + 1
            
            output[index] = 1 if res < 1 else res
        
        return output 

            




