import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list.
        """
        # Min-heap to efficiently get the smallest element across all k lists
        min_heap = []
        
        # Step 1: Add the head of each linked list to the heap
        for i, node in enumerate(lists):
            if node:  # Check if the list is not empty
                # Push a tuple (node value, list index, node itself) to the heap
                heapq.heappush(min_heap, (node.val, i, node))
        
        # Step 2: Create a dummy node to build the merged linked list
        dummy_node = ListNode()
        curr = dummy_node  # Pointer to the current node in the merged list
        
        # Step 3: Process the heap until it is empty
        while min_heap:
            # Pop the smallest element from the heap
            val, ind, node = heapq.heappop(min_heap)
            
            # Add this node to the merged list
            curr.next = node
            curr = node  # Move the current pointer to the newly added node
            
            # If the popped node has a next node, push it to the heap
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, ind, node))
        
        # Step 4: Return the merged list starting from the node after the dummy
        return dummy_node.next

# Time Complexity:
# - Each node is added and removed from the heap once.
# - Heap operations (push and pop) take O(log k), where k is the number of linked lists.
# - Since there are a total of N nodes across all lists, the overall time complexity is:
#   O(N log k)

# Space Complexity:
# - The heap stores at most k nodes at any given time.
# - Thus, the space complexity for the heap is O(k).