# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        
        def reversell(temp):
            
            prev = None
            
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
            return prev
            
        
        def find_kthnode(temp,k):
            
            k -= 1
            
            while temp is not None and k > 0:
                k -= 1
                temp = temp.next
                
            return temp
        
        
        
        
        
        temp = head
        
        prev_node = None
        
        while temp:
            
            kthnode = find_kthnode(temp,k)
            
            
            if kthnode == None:
                prev_node.next = temp
                
                break
            
            next_node = kthnode.next
            kthnode.next = None
            
            reversell(temp)
            
            if temp == head:
                head = kthnode
            else:  
                prev_node.next = kthnode
                
            prev_node = temp
            temp = next_node
            
        return head
            
            
            
            
            