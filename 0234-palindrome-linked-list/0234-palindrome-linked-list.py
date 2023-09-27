# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Check if the linked list is empty or has only one element,
        # which is considered a palindrome.
        if not head or not head.next:
            return True

        # Define a function to reverse a linked list.
        def revll(ptr):
            prev = None
            next_node = None
            while ptr:
                next_node = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = next_node
            return prev

        # Initialize slow and fast pointers for finding the middle of the list.
        slow = head
        fast = head

        # Move the pointers to find the middle.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list starting from slow.next.
        slow.next = revll(slow.next)

        # Move slow to the beginning of the reversed second half,
        # and initialize a dummy pointer at the head of the original list.
        slow =  slow.next
        dummy = head

        # Compare values from the first half with values from the reversed second half.
        while slow:
            if dummy.val != slow.val:
                return False
            else:
                dummy = dummy.next
                slow = slow.next

        # If the loop completes without finding any mismatches, it's a palindrome.
        return True
