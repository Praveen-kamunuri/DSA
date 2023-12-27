# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Convert the linked list to a Python list
        li = []  # Initialize an empty list to store values from the linked list
        current = head  # Start from the head of the linked list
        while current:
            li.append(current.val)  # Append the value of the current node to the list
            current = current.next  # Move to the next node

        # Step 2: Sort the Python list
        li.sort()  # Sort the list in ascending order

        # Step 3: Update the linked list with the sorted values
        current = head  # Reset the current pointer to the head of the linked list
        for i in range(len(li)):
            current.val = li[i]  # Update the value of the current node with the sorted value
            current = current.next  # Move to the next node

        # Step 4: Return the sorted linked list
        return head  # Return the head of the sorted linked list

# This implementation uses extra space to store the values in a Python list, which results in O(n) space complexity.
# Even if you delete the list afterward, the space complexity remains O(n).
# To achieve O(1) space complexity, you would need to use an in-place sorting algorithm designed for linked lists.
