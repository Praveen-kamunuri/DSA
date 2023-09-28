# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the list is empty or has only one node (no middle to delete)
        if not head or not head.next:
            return None

        # Create a dummy node 'start' to simplify handling edge cases
        start = ListNode()
        start.next = head  # Point 'start.next' to the head of the linked list

        # Initialize two pointers, 'slow' and 'fast'
        slow = start
        fast = head

        # Move 'slow' one step at a time and 'fast' two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'slow' is now pointing to the middle node
        # Remove the middle node by updating the pointers
        slow.next = slow.next.next

        # Return the modified list with the middle node removed
        return head
