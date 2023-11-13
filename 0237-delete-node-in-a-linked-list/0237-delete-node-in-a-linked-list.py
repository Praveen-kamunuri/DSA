# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # Check if the given node or its next node is None
        if node is None or node.next is None:
            # You cannot delete the last node or a node that doesn't exist.
            return

        # Copy the value of the next node to the current node
        next_node = node.next
        node.val = next_node.val

        # Update the next pointer of the current node to point to the node after the next node
        node.next = next_node.next
