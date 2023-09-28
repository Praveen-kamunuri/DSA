# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node 'start' to simplify handling edge cases
        start = ListNode()
        start.next = head  # Point 'start.next' to the head of the linked list
        
        # Initialize two pointers, 'slow' and 'fast', both starting at 'start'
        slow = start
        fast = start
        
        # Move the 'fast' pointer n+1 positions ahead
        for i in range(1, n + 1):
            fast = fast.next
        
        # Move both 'slow' and 'fast' until 'fast' reaches the end of the list
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Now, 'slow' is at the node just before the one to be removed
        # Update the pointers to remove the node
        slow.next = slow.next.next
        
        # Return the modified list, excluding the removed node
        return start.next
