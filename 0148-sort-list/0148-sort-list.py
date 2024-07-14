from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeSortedList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2
        
        return dummy.next

    def findMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        middle = self.findMiddle(head)
        left = head
        right = middle.next
        middle.next = None
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeSortedList(left, right)

# Time Complexity (TC): O(n log n)
# The algorithm follows a divide-and-conquer approach, where the list is divided into two halves 
# (log n divisions) and each division involves a linear traversal to merge the sorted halves (n work per division). 
# Thus, the overall time complexity is O(n log n).

# Space Complexity (SC): O(log n)
# The space complexity is O(log n) due to the recursion stack used in the sortList function. 
# Although the merge process itself is done in constant space, the recursion depth will be log n, making the overall space complexity O(log n).
