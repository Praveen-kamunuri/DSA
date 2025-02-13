from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string using level-order traversal (BFS).
        
        :type root: TreeNode
        :rtype: str
        """

        # If the tree is empty, return an empty string
        if not root:
            return ""

        s = ""  # String to store serialized data
        q = deque()  # Queue for BFS traversal
        q.append(root)

        while q:
            node = q.popleft()

            if not node:
                s += '#,'  # Use '#' to denote null nodes
            else:
                s += str(node.val) + ','  # Store node value
                q.append(node.left)  # Add left child to queue
                q.append(node.right)  # Add right child to queue

        return s[:-1]  # Remove the trailing comma


    def deserialize(self, data):
        """Decodes the serialized string back to a binary tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # If the serialized data is empty, return None
        if not data:
            return None

        q = deque()  # Queue to help reconstruct the tree
        tokens = data.split(',')  # Split the serialized data

        root = TreeNode(int(tokens.pop(0)))  # Create the root node
        q.append(root)

        while q and tokens:
            node = q.popleft()

            if tokens:
                left_val = tokens.pop(0)
                if left_val != '#':  # If not null, create left child
                    left_node = TreeNode(int(left_val))
                    node.left = left_node
                    q.append(left_node)

            if tokens:
                right_val = tokens.pop(0)
                if right_val != '#':  # If not null, create right child
                    right_node = TreeNode(int(right_val))
                    node.right = right_node
                    q.append(right_node)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
Time Complexity:
- serialize: O(N), since we traverse each node once during BFS.
- deserialize: O(N), since we reconstruct each node once.

Space Complexity:
- serialize: O(N), for storing the serialized output string.
- deserialize: O(N), for storing the queue during BFS.
"""
