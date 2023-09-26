class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Function to reverse a linked list in-place
        def reverse_linked_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        slow = head
        fast = head
        
        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        second_half = reverse_linked_list(slow)
        
        # Compare the first half with the reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
