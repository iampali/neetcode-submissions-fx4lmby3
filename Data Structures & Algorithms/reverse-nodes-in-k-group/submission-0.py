# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseGroup(head, left, right):
            if left == right:
                return head
            
            dummy = ListNode(0, head)
            prev = dummy

            for _ in range(left - 1):
                prev = prev.next
            
            curr = prev.next

            for _ in range(right - left):
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            
            return dummy.next
        
        total = 0
        curr = head
        while curr:
            curr = curr.next
            total += 1
        
        print(total)
        for i in range(total):
            if i % k == 0 and (i + k) <= total:
                print(f"Running for i {i}")
                head = reverseGroup(head, i + 1, i + k)
        
        return head



        
