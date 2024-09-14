class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        if self.capacity  == len(self.hashmap):
            self._remove(self.tail.prev)
        self._insert(Node(key, value))
        
    def _insert(self, node):
        self.hashmap[node.key] = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next.prev = node
        
    def _remove(self, node):
        del self.hashmap[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)