# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, tortoise and rabbit
        tortoise = head
        rabbit = head
        while rabbit and rabbit.next:
            # Move tortoise one step and rabbit two steps at a time
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            # Check if tortoise and rabbit meet at the same node (cycle detected)
            if tortoise == rabbit:
                return True
        # If the loop completes without finding a cycle, return False
        return False
