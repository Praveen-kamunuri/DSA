class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to start the merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists until one of them becomes empty
        while list1 and list2:
            # Compare the values of the current nodes in both lists
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes of the non-empty list
        current.next = list1 if list1 else list2
        
        # Return the head of the merged list
        return dummy.next
