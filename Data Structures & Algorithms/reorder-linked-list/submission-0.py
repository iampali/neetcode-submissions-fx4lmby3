# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # ll -> [0, 1, 2, 3, 4, 5, 6]
        
        # find the middle using fast and slow pointer -> 4
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the ll from middle to last -> [0(i), 1, 2, 3, 6(j), 5, 4] 
        curr = slow.next
        prev = slow.next = None
            
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        # start the i from head and j from middle and just reorder them -> [0,6,1,5,2,4,3]

        i, j = head, prev

        while i and j:
            temp1 = i.next
            temp2 = j.next 
            i.next = j
            j.next = temp1
            i = temp1
            j = temp2