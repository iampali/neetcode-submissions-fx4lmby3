"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}

        curr = head
        new_head = None

        while curr:
            if curr not in visited:
                root = Node(curr.val)
                visited[curr] = root
            else:
                root = visited[curr]
            
            if not new_head:
                new_head = root
            
            if curr.next:
                if curr.next not in visited:
                    root.next = Node(curr.next.val)
                    visited[curr.next] = root.next
                else:
                    root.next = visited[curr.next]
            
            if curr.random:
                if curr.random not in visited:
                    root.random = Node(curr.random.val)
                    visited[curr.random] = root.random
                else:
                    root.random = visited[curr.random]
            
            curr = curr.next

        return new_head

            


