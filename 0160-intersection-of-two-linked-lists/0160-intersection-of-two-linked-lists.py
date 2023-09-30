# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1 = headA
        h2 = headB
        while h1 != h2:
            if h1 is None:
                h1 = headB
            else:
                h1 = h1.next
            if h2 is None:
                h2 = headA
            else:
                h2 = h2.next
        return h1
            
        