class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize two pointers, h1 and h2, to the heads of the input linked lists.
        h1 = headA
        h2 = headB

        # Iterate until h1 and h2 meet or both reach the end (None) of their respective lists.
        while h1 != h2:
            # If h1 reaches the end of list A, move it to the head of list B.
            if h1 is None:
                h1 = headB
            else:
                # Otherwise, move h1 to the next node in list A.
                h1 = h1.next
            
            # If h2 reaches the end of list B, move it to the head of list A.
            if h2 is None:
                h2 = headA
            else:
                # Otherwise, move h2 to the next node in list B.
                h2 = h2.next
        
        # If h1 and h2 meet, they have found the intersection point (or reached the end, which is None).
        # Return the intersection point (or None if there's no intersection).
        return h1
