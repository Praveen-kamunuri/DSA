class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the result list.
        dummy = ListNode()
        temp = dummy  # Initialize a temporary pointer to the dummy node.
        carry = 0  # Initialize carry to 0.

        # Loop until both input lists are empty and there is no carry left.
        while l1 or l2 or carry:
            # Calculate the sum of values from l1, l2, and carry.
            summ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = summ // 10  # Calculate the carry for the next iteration.

            # Create a new node with the value of (summ % 10) and add it to the result list.
            temp.next = ListNode(summ % 10)
            temp = temp.next  # Move the temp pointer to the newly added node.

            # Move to the next nodes in l1 and l2 if they exist.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list, starting from the node after the dummy node.
        return dummy.next
