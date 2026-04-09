# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        ans = 0
        i = 0
        while l1:
            ans += l1.val * 10**i
            i += 1
            l1 = l1.next
        
        i = 0
        while l2:
            ans += l2.val * 10**i
            i += 1
            l2 = l2.next

        if ans == 0:
            return ListNode(0)
        
        def helper(val):
            if val == 0:
                return None
            
            n = val % 10
            root = ListNode(n)

            root.next = helper(val//10)

            return root

        return helper(ans)
        
        