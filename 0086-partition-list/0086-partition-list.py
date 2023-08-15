# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        less_head = ListNode()  # Dummy node for nodes less than x
        less_tail = less_head   # Pointer to the tail of the 'less' list
        greater_head = ListNode()  # Dummy node for nodes greater than or equal to x
        greater_tail = greater_head  # Pointer to the tail of the 'greater' list

        current = head  # Pointer to traverse the original list

        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next

        # Connect the two lists and set the last node's next pointer to None
        less_tail.next = greater_head.next
        greater_tail.next = None

        return less_head.next

        