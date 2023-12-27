# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        temp = head
        while temp:
            li.append(temp.val)
            temp = temp.next
        
        li.sort()
        
        temp = head
        for i in range(len(li)):
            temp.val = li[i]
            temp = temp.next
        
        return head