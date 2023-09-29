# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        current = head
        while current:
            li.append(current.val)
            current = current.next
        li.sort()
        current = head
        for i in range(len(li)):
            current.val = li[i]
            current = current.next
        return head
            
        