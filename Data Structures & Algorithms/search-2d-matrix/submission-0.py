class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m ,n = len(matrix), len(matrix[0])
        start1, start2, end1, end2 = 0, 0, m-1, n-1
        while(start1 <= end1 and start2 <= end2):
            mid = ( (start1 + end1)//2, (start2 + end2) // 2 )
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] < target:
                if mid[1] == n-1:
                    start1 = mid[0] + 1
                    start2 = 0
                else:
                    start2 = mid[1] + 1
            else:
                if mid[1] == 0:
                    end1 = mid[0] - 1
                    end2 = n-1
                else:
                    end2 = mid[1] - 1

        return False 