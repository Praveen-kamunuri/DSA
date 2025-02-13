from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        s = ""

        q = deque()
        
        q.append(root)

        while q:
            node = q.popleft()

            if not node:
                s += '#,'

            else:
                s += str(node.val) + ','

                q.append(node.left)
                q.append(node.right)

        return s[:-1]



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        q = deque()

        tokens = data.split(',')

        root = TreeNode(int(tokens.pop(0)))

        q.append(root)

        while q and tokens:

            node = q.popleft()

            if tokens:

                left_val = tokens.pop(0)

                if left_val != '#':
                    left_node = TreeNode(int(left_val))

                    node.left = left_node

                    q.append(left_node)

            if tokens:

                right_val = tokens.pop(0)

                if right_val != '#':
                    right_node = TreeNode(int(right_val))

                    node.right = right_node

                    q.append(right_node)

        return root

            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))