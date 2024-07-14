# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Handle cases where the list is empty or has only one node
        if not head or not head.next:
            return None
        
        # Initialize a dummy node to simplify edge case handling
        start = ListNode()
        start.next = head
        
        # Initialize two pointers, slow and fast, both pointing to the dummy node
        slow = start
        fast = start
        
        # Move fast pointer n+1 steps ahead
        for i in range(1, n + 1):
            fast = fast.next
        
        cnt = 1  # To keep track of the number of iterations
        # Move both slow and fast pointers until fast reaches the end of the list
        while fast.next:
            slow = slow.next
            fast = fast.next
            cnt += 1
        
        # If cnt is 1, it means we need to remove the head node
        if cnt == 1:
            head = head.next
        else:
            # Otherwise, remove the nth node from the end
            slow.next = slow.next.next
        
        # Return the updated list, which may have a new head if the original head was removed
        return head

# Time Complexity (TC): O(L)
# The function makes a single pass through the list to position the fast pointer, 
# and another pass through the list to find and remove the nth node from the end. 
# Therefore, the time complexity is O(L), where L is the length of the list.

# Space Complexity (SC): O(1)
# The function uses a constant amount of extra space (for pointers and counters), 
# so the space complexity is O(1).
