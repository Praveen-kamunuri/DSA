# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to form the result linked list
        dummy = ListNode(-1)
        temp = dummy
        carry = 0
        
        # Traverse through both linked lists
        while l1 is not None or l2 is not None:
            summ = 0
            
            # Add values from l1 if available
            if l1:
                summ += l1.val
                l1 = l1.next
            
            # Add values from l2 if available
            if l2:
                summ += l2.val
                l2 = l2.next
            
            # Add carry from previous summation
            summ += carry
            
            # Calculate new carry
            carry = summ // 10
            
            # Create new node with the summation value's unit place
            node = ListNode(summ % 10)
            temp.next = node
            temp = temp.next
        
        # If there is any carry left, create a new node for it
        if carry:
            node = ListNode(carry)
            temp.next = node
        
        # Return the next of dummy node which is the head of the resultant list
        return dummy.next

# Time Complexity (TC):
# The time complexity is O(max(N, M)), where N and M are the lengths of l1 and l2 respectively.
# This is because we iterate through each node of both lists exactly once.

# Space Complexity (SC):
# The space complexity is O(max(N, M)) as well, since we are creating a new linked list that
# contains at most max(N, M) + 1 nodes (one additional node for a possible carry at the end).
