# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []

        slow, fast = head, head

        while fast and fast.next:
            temp.append(slow)
            slow = slow.next
            fast = fast.next.next

        output = float("-inf")
        i = len(temp) - 1
        while slow:
            output = max(output, temp[i].val + slow.val)
            i -= 1
            slow = slow.next
        
        return output
