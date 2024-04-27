class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Check if head is None
        if head is None:
            return None
        
        # Create a dummy node to handle cases where the head node needs to be removed
        dummy = ListNode(-1)
        dummy.next = head
        
        # Initialize current node as the dummy node
        current = dummy
        
        # Traverse the list
        while current.next:
            # Check if the next node's value is equal to val
            if current.next.val == val:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the head of the modified list (excluding the dummy node)
        return dummy.next
