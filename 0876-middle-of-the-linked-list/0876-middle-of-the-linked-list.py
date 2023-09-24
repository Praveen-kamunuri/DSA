# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        rabbit = head
        while rabbit and rabbit.next:
            tortoise  = tortoise.next
            rabbit = rabbit.next.next
        return tortoise