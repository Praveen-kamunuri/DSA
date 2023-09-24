# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        cnt = 1
        while current.next != None:
            current = current.next
            cnt += 1
        
        mid = ( cnt // 2) + 1
        print(mid)
        i = 1
        current = head
        while i <= mid-1:
            current = current.next
            i += 1
        head = current
        return head