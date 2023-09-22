# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # Copy the value of the next node to the current node
        node.val = node.next.val
        
        # Update the next pointer of the current node to skip the next node
        node.next = node.next.next
