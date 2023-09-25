# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create an empty list to store visited nodes
        visited_nodes = []

        # Start at the head of the linked list
        current = head

        # Traverse the linked list
        while current:
            # Check if the current node is already in the visited nodes list
            if current not in visited_nodes:
                # If not, add it to the list and move to the next node
                visited_nodes.append(current)
                current = current.next
            else:
                # If the current node is in the visited nodes list, a cycle is detected
                return True

        # If the loop completes without finding a cycle, return False
        return False
