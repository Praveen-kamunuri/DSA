# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
            
        
        
        
        def revll(ptr):
            prev = None
            next_node = None
            while ptr:
                next_node = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = next_node
            return prev
        
        
        
        
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = revll(slow.next)
        
        slow =  slow.next
        while slow:
            if head.val != slow.val:
                return False
            else:
                head = head.next
                slow = slow.next
        return True
                
