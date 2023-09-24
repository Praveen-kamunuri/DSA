# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, tortoise and rabbit, both starting at the head
        tortoise = head
        rabbit = head
        
        # Traverse the list with tortoise moving one step and rabbit moving two steps
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
        
        # When rabbit reaches the end (or None), tortoise will be at the middle node
        return tortoise
