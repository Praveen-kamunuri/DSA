# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Step 1: Insert a copied node right after each original node
        def insertCopyInBetween(head):
            temp = head
            while temp:
                copy = Node(temp.val)  # Create a copy of the current node
                copy.next = temp.next  # Point the copy's next to the original node's next
                temp.next = copy  # Insert the copy node right after the original node
                temp = temp.next.next  # Move to the next original node
            return head
        
        # Step 2: Connect the random pointers of the copied nodes
        def connectRandomPointers(head):
            temp = head
            while temp:
                copy = temp.next  # Get the copied node
                if temp.random:
                    copy.random = temp.random.next  # Connect the copy's random pointer
                temp = temp.next.next  # Move to the next original node
            return head
        
        # Step 3: Extract the deep copy list and restore the original list
        def getDeepCopyList(head):
            dummy = Node(-1)  # Dummy node to help extract the deep copy list
            res = dummy
            temp = head
            while temp:
                res.next = temp.next  # Get the copied node
                res = res.next  # Move to the next node in the deep copy list
                temp.next = temp.next.next  # Restore the original list
                temp = temp.next  # Move to the next original node
            return dummy.next  # Return the head of the deep copy list
        
        if not head:
            return None  # If the original list is empty, return None
        
        insertCopyInBetween(head)  # Step 1: Insert copies in between
        connectRandomPointers(head)  # Step 2: Connect random pointers
        return getDeepCopyList(head)  # Step 3: Extract deep copy list

# Time Complexity (TC):
# The algorithm consists of three passes over the list:
# 1. Insert copies in between the original nodes: O(n)
# 2. Connect random pointers for the copied nodes: O(n)
# 3. Extract the deep copy list and restore the original list: O(n)
# Overall TC: O(n), where n is the number of nodes in the original list.

# Space Complexity (SC):
# The algorithm uses a few pointers and a dummy node, all of which take constant space.
# Therefore, the space complexity is O(1) (excluding the space for the new nodes, which is necessary for the deep copy).
