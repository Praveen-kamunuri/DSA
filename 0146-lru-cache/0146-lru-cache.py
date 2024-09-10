class Node:
    # Node class to represent each entry in the doubly linked list
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRUCache with the given capacity
        self.capacity = capacity
        self.map = {}  # HashMap to store the cache keys and corresponding nodes
        self.head = Node(0, 0)  # Dummy head node for the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail node for the doubly linked list
        self.head.next = self.tail  # Connect head to tail initially
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Retrieve the value from the cache, and update it as most recently used
        if key in self.map:
            node = self.map[key]
            self._remove(node)  # Remove the node from its current position
            self._insert(node)  # Insert it back as the most recently used
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # Insert or update the value in the cache
        if key in self.map:
            # If the key is already in cache, remove the old node
            self._remove(self.map[key])
        if len(self.map) == self.capacity:
            # If the cache is full, remove the least recently used (LRU) node
            self._remove(self.tail.prev)
        # Insert the new node as the most recently used
        self._insert(Node(key, value))

    def _remove(self, node: Node) -> None:
        # Remove the node from the doubly linked list
        del self.map[node.key]  # Remove it from the HashMap
        node.prev.next = node.next  # Bypass the node from the list
        node.next.prev = node.prev

    def _insert(self, node: Node) -> None:
        # Insert the node as the most recently used, right after the head
        self.map[node.key] = node  # Add it to the HashMap
        node.next = self.head.next  # Point the node to the current first node
        self.head.next.prev = node  # Connect the current first node back to this new node
        self.head.next = node  # Move the head's next to this new node
        node.prev = self.head  # Make the new node's prev point to the head

# Time Complexity: O(1) for both get and put operations because the operations on the doubly linked list and HashMap are O(1).
# Space Complexity: O(N), where N is the capacity of the cache, because we're storing N nodes in the doubly linked list and HashMap.
