# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Helper function to reverse a linked list
        def revll(current):
            prev = None
            next_node = None
            
            # Reverse the linked list
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        # Edge case: if the list is empty or has only one node, it is a palindrome
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        
        # Use slow and fast pointers to find the middle of the list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half of the list
        new_head = revll(slow.next)
        
        d1 = head
        d2 = new_head
        
        # Compare the first half and the reversed second half of the list
        while d2:
            if d1.val != d2.val:
                # If they don't match, reverse the second half back to its original form (optional)
                revll(new_head)
                return False
            
            d1 = d1.next
            d2 = d2.next
            
        # If all nodes matched, return True
        return True

# Time Complexity (TC):
# - Finding the middle of the list: O(n)
# - Reversing the second half of the list: O(n/2) = O(n)
# - Comparing the two halves: O(n/2) = O(n)
# - Restoring the original list (if desired): O(n/2) = O(n)

# The overall time complexity is O(n).

# Space Complexity (SC):
# - The algorithm uses a constant amount of extra space for pointers and variables.

# The overall space complexity is O(1).
