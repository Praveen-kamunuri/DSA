# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reversell(temp):
            """Reverse the linked list starting from `temp`."""
            prev = None
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
            return prev
        
        def find_kthnode(temp, k):
            """Find the k-th node starting from `temp`. Return None if there are fewer than k nodes."""
            k -= 1
            while temp is not None and k > 0:
                k -= 1
                temp = temp.next
            return temp
        
        temp = head
        prev_node = None
        
        while temp:
            kthnode = find_kthnode(temp, k)
            
            # If there are fewer than k nodes left, connect the previous part and break the loop.
            if kthnode is None:
                if prev_node:
                    prev_node.next = temp
                break
            
            # Store the next node after the k-th node.
            next_node = kthnode.next
            kthnode.next = None
            
            # Reverse the list starting from temp and connect it properly.
            reversell(temp)
            
            if temp == head:
                head = kthnode
            else:
                prev_node.next = kthnode
            
            # Update prev_node to the end of the reversed segment.
            prev_node = temp
            temp = next_node
        
        return head

# Time Complexity (TC):
# The time complexity is O(N), where N is the number of nodes in the linked list.
# This is because each node is processed a constant number of times (once to find the k-th node and once to reverse the segment).

# Space Complexity (SC):
# The space complexity is O(1) as no additional space proportional to the input size is used. Only a few pointers are used for manipulation.
