# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        if node is None or node.next is None:
            # You cannot delete the last node or a node that doesn't exist.
            return

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
