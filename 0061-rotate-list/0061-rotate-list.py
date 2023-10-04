# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if the linked list is empty
        if not head:
            return None
        
        # Find the length of the linked list
        current = head
        length = 1
        while current.next is not None:
            length += 1
            current = current.next
        
        # Make the linked list circular by connecting the last node to the head
        current.next = head
        
        # Calculate the effective rotation value (k % length)
        k = k % length
        
        # Calculate the destination position where rotation ends
        dest = (length - k)
        
        # Traverse the linked list to the destination position
        cnt = 1
        current = head
        while cnt != dest:
            cnt += 1
            current = current.next
        
        # Update the head to the new rotated position
        head = current.next
        
        # Set the current node's next to None to break the circular connection
        current.next = None
        
        # Return the new head of the rotated linked list
        return head
