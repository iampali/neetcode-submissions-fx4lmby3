# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        left_node, right_node, prev_left = None, None, None
        i = 1
        while curr:
            print(i)

            if i == left:
                left_node = curr
                print(f"Found left as {left_node.val}")
            if i == right:
                right_node = curr
                print(f"Found right as {right_node.val}")
                break
            
            if not left_node:
                prev_left = curr
            
            curr = curr.next
            i += 1
        
        print(f"Found prev as {prev_left.val if prev_left else None}")
        prev = left_node
        curr = left_node.next
        right_next = right_node.next
        while(curr != right_next):
            print(f"curr is {curr.val}")
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if prev_left:
            prev_left.next = right_node
        left_node.next = curr

        if left_node == head:
            return right_node
        
        return head
