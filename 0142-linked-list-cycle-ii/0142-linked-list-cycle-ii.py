# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return None
        
        
        
        
        rabbit = head
        tortoise = head
        entry = head
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise == rabbit:
                while entry != tortoise:
                    entry = entry.next
                    tortoise = tortoise.next
                return entry
        return None