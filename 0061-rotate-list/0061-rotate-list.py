# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        current = head
        length = 1
        while current.next is not None:
            length += 1
            current = current.next
        current.next = head
        
        k = k % length 
        dest = ( length - k )
        cnt = 1
        current = head
        while cnt != dest:
            cnt += 1
            current = current.next
        head  = current.next
        current.next = None
        return head
        
        