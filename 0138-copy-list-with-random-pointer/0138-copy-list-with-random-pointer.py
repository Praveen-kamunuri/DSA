"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        def insertCopyInBetween(head):
            
            temp = head
            
            while temp:
                copy = Node(temp.val)
                copy.next = temp.next
                temp.next = copy
                temp = temp.next.next
            return head
        
        def connectRandomPointers(head):
            temp = head
            
            while temp:
                copy = temp.next
                if temp.random:
                    copy.random = temp.random.next
                else:
                    copy.random = None
                
                temp = temp.next.next
            return head
        
        def getDeepCopyList(head):
            
            dummy = Node(-1)
            res = dummy
            
            temp = head
            
            while temp:
                res.next = temp.next
                res = res.next
                temp.next = temp.next.next
                temp = temp.next
            return dummy.next
            
            
        
        
                
        
        
        insertCopyInBetween(head)
        connectRandomPointers(head)
        return getDeepCopyList(head)
        