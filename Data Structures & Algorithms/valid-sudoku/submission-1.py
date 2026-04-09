class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_valid(nums):
            temp = {}
            #print(nums)
            for i in nums:
                if i in temp and i != '.':
                    return False
                temp[i] = True
            return True

        def get_num(i,j, board):
            nums = []
            for a in range(i-2, i+1):
                for b in range(j-2, j+1):
                    nums.append(board[a][b])
            
            return nums
        
        for i in board:
            if not check_valid(i):
                return False
        for col in range(9):
            a = [board[row][col] for row in range(9)]
            if not check_valid(a):
                return False
        for i in [2,5,8]:
            for j in [2,5,8]:
                nums = get_num(i, j , board)
                if not check_valid(nums):
                    return False
        
        return True
        