# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
          

        def merge_two_Lists(node1, node2):
        
            if not node1 and not node2:
                return None
        
            elif node1 and node2:
                if node1.val < node2.val:
                    val = node1.val
                    next1 = node1.next
                    next2 = node2
                else:
                    val = node2.val
                    next1 = node1
                    next2 = node2.next
                
            
            elif node1:
                val = node1.val
                next1 = node1.next
                next2 = None
            
            elif node2:
                val = node2.val
                next1 = None
                next2 = node2.next
            
            root = ListNode(val)

            root.next = merge_two_Lists(next1, next2)

            return root
        
        result = None
        for k in lists:
            result = merge_two_Lists(result, k)
        
        return result



