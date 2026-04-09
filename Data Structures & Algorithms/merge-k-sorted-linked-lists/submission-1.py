# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
          

        def merge_two_Lists(node1, node2):
            dummy = ListNode()
            tail = dummy

            while node1 and node2:
                if node1.val < node2.val:
                    tail.next = node1
                    node1 = node1.next
                else:
                    tail.next = node2
                    node2 = node2.next
                
                tail = tail.next
            
            if node1:
                tail.next = node1
            if node2:
                tail.next = node2
            
            return dummy.next
        
        result = None
        for k in lists:
            result = merge_two_Lists(result, k)
        
        return result



