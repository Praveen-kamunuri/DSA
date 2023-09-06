class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the number of nodes in each part and the number of nodes with an extra node
        part_size = length // k
        extra_nodes = length % k

        result = []
        current = head
        prev = None
        
        for i in range(k):
            result.append(current)
            part_length = part_size + (1 if i < extra_nodes else 0)

            for j in range(part_length):
                prev = current
                current = current.next if current else None
            
            if prev:
                prev.next = None

        return result
