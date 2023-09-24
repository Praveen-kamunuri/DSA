# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        current = head   # Current node
        prev = None      # Previous node

        # Iterate through the list and reverse the pointers
        while current:
            next_node = current.next   # Temporary variable to store the next node
            current.next = prev       # Reverse the next pointer of the current node
            prev = current            # Move prev to the current node
            current = next_node       # Move current to the next node

        # Update the head to the new head (prev)
        head = prev

        # Return the new head of the reversed list
        return head
