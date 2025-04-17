# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root, reverse):
        self.stack = []
        self.reverse = reverse  # True for reverse in-order, False for normal in-order
        self._push_all(root)    # Preload the stack

    def _push_all(self, node):
        # Push all nodes along the path to the extreme (leftmost or rightmost)
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right  # Reverse in-order: go right
            else:
                node = node.left   # Normal in-order: go left

    def next(self):
        # Return the next value in the traversal
        node = self.stack.pop()
        if self.reverse:
            self._push_all(node.left)  # For reverse, go to left subtree
        else:
            self._push_all(node.right) # For normal, go to right subtree
        return node.val


class Solution:
    def findTarget(self, root, k):
        if not root:
            return False

        # Create two iterators:
        left_iter = BSTIterator(root, reverse=False)   # Start from smallest (in-order)
        right_iter = BSTIterator(root, reverse=True)   # Start from largest (reverse in-order)

        i = left_iter.next()
        j = right_iter.next()

        # Use two pointers technique
        while i < j:
            total = i + j
            if total == k:
                return True
            elif total < k:
                i = left_iter.next()   # Need larger value
            else:
                j = right_iter.next()  # Need smaller value

        return False  # No such pair found


# Time Complexity:
# - Each node is visited once by either of the two iterators => O(n)

# Space Complexity:
# - Stack stores height of tree in worst case => O(h), where h is the height of the tree
# - Total space: O(h) for each iterator => O(h)

# Overall:
# TC: O(n)
# SC: O(h)
