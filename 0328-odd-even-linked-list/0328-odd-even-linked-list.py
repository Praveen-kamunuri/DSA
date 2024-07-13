# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the list is empty or has only one node
        if not head or not head.next:
            return head  # No reordering needed
        
        # Initialize pointers for odd and even lists
        odd = head
        even = head.next
        even_head = head.next  # To connect the end of odd list to the start of even list
        
        # Traverse the list, rearranging nodes into odd and even lists
        while even and even.next:
            odd.next = odd.next.next  # Link current odd node to the next odd node
            even.next = even.next.next  # Link current even node to the next even node
            
            # Move odd and even pointers to the next nodes in their respective lists
            odd = odd.next
            even = even.next
        
        # Connect the end of the odd list to the head of the even list
        odd.next = even_head
        
        return head  # Return the rearranged list's head

# Time Complexity (TC): O(n)
# The list is traversed once, so the time complexity is O(n), where n is the number of nodes in the list.

# Space Complexity (SC): O(1)
# The space complexity is O(1) because we are using a constant amount of extra space (pointers).
