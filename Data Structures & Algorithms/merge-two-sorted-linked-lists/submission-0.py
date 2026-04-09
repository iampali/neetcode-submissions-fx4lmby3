# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        
        if list1 and list2:
            if list1.val < list2.val:
                val = list1.val
                next1 = list1.next
                next2 = list2
            else:
                val = list2.val
                next1 = list1
                next2 = list2.next
        elif list1:
            val = list1.val
            next1 = list1.next
            next2 = None
        else:
            val = list2.val
            next1 = None
            next2 = list2.next


        root = ListNode(val)
        


        root.next = self.mergeTwoLists(next1, next2)

        return root

            

