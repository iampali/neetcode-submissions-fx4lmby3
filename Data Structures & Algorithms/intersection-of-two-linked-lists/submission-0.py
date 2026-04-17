# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curr = headA

        while curr:
            curr2 = headB
            while curr2:
                if curr == curr2:
                    return curr
                
                curr2 = curr2.next
            
            curr = curr.next
        
        return None