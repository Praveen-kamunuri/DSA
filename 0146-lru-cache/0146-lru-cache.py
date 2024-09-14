class Node:
    # Doubly linked list node with a key-value pair
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class LRUCache:

    # Initialize the LRUCache with a given capacity
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum capacity of the cache
        self.hashmap = {}  # Hashmap to store keys and corresponding nodes
        self.head = Node(0, 0)  # Dummy head of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail of the doubly linked list
        self.head.next = self.tail  # Initialize the list as head <-> tail
        self.tail.prev = self.head

    # Get the value of the key if it exists in the cache, otherwise return -1
    def get(self, key: int) -> int:
        if key in self.hashmap:
            # If key exists, remove it from its current position and re-insert at the front
            node = self.hashmap[key]
            self._remove(node)  # Remove node from its current position
            self._insert(node)  # Re-insert node at the head (front of the list)
            return node.val
        else:
            # Return -1 if the key is not present in the cache
            return -1

    # Add or update the key-value pair in the cache
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # If key already exists, remove it from the cache
            self._remove(self.hashmap[key])
        if self.capacity == len(self.hashmap):
            # If the cache is full, remove the least recently used (LRU) node, i.e., the node before the tail
            self._remove(self.tail.prev)
        # Insert the new key-value pair into the cache
        self._insert(Node(key, value))

    # Internal method to insert a node at the front (most recently used) position
    def _insert(self, node):
        self.hashmap[node.key] = node  # Add the node to the hashmap
        node.next = self.head.next  # Node's next pointer points to the current first node
        self.head.next.prev = node  # Current first node's prev pointer points to the new node
        self.head.next = node  # Head's next points to the new node
        node.prev = self.head  # New node's prev points to the head

    # Internal method to remove a node from its current position in the linked list
    def _remove(self, node):
        del self.hashmap[node.key]  # Remove the node from the hashmap
        node.prev.next = node.next  # Adjust the previous node's next pointer
        node.next.prev = node.prev  # Adjust the next node's prev pointer


# Example usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
