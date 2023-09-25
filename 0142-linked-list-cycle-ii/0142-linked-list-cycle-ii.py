# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty or has only one node
        if not head or head.next is None:
            return None  # No cycle
        
        # Initialize two pointers, rabbit and tortoise
        rabbit = head
        tortoise = head
        
        # Initialize an entry point for cycle detection
        entry = head
        
        # Use Floyd's Tortoise and Hare algorithm to detect a cycle
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            
            # When a cycle is detected, find the node where it begins
            if tortoise == rabbit:
                while entry != tortoise:
                    entry = entry.next
                    tortoise = tortoise.next
                return entry
        
        # If no cycle is found, return None
        return None  # No cycle
