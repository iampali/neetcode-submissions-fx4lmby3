class Solution:
    def validPalindrome(self, s: str) -> bool:
        self.deletedFlag = False
        
        def check_palindrome(temp):
            i, j = 0, len(temp)-1
            while(i < j):
                if temp[i] != temp[j]:
                    if self.deletedFlag : 
                        print(f"Found deleteed flag is True  i and j values {i} and {j}")
                        return False
                    self.deletedFlag = True
                    print(f"changed deleteed  flag value to true for  i and j values {i} and {j}")
                    delete_i = check_palindrome(temp[i+1:j+1])
                    delete_j = check_palindrome(temp[i:j])
                    print(f"deleted i return {delete_i} for i and j values {i} and {j}")
                    print(f"deleted j return {delete_j} for i and j values {i} and {j}")

                    return delete_i or delete_j

                i+=1
                j-=1
            
            return True
        
        return check_palindrome(s)