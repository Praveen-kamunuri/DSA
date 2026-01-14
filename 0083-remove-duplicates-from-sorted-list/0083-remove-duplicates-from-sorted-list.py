# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Pointer to traverse the linked list
        curr = head
        
        # Traverse the entire linked list
        while curr:
            # If the current node and the next node have the same value
            # we skip the next node by pointing current.next to next.next
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next  # Remove duplicate
            else:
                # Otherwise, move to the next node
                curr = curr.next
        
        # Return the modified list without duplicates
        return head


"""
Time Complexity (TC):
- Each node is visited once → O(n), 
  where n = number of nodes in the linked list.

Space Complexity (SC):
- No extra data structures used → O(1) (constant extra space).
"""
