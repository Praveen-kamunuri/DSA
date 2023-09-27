# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(ptr):
            pre = None
            nex = None
            while ptr != None:
                nex = ptr.next
                ptr.next = pre
                pre = ptr
                ptr = nex
            return pre

    
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        slow.next = reverse(slow.next)
        slow = slow.next
        dummy = head
        while slow != None:
            if dummy.val != slow.val:
                return False
            dummy = dummy.next
            slow = slow.next
        return True
     



