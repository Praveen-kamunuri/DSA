# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def revll(current):
            prev = None
            next_node = None
            
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        
        
        
        
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        new_head = revll(slow.next)
        
        
        d1 = head
        d2 = new_head
        
        while d2:
            if d1.val != d2.val:
                revll(new_head)
                return False
            
            d1 = d1.next
            d2 = d2.next
            
        return True
    