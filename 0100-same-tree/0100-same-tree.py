# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, the trees are identical at this point
        if not p and not q:
            return True
        
        # If either node is None or the values are different, the trees are not identical
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check if the left and right subtrees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time Complexity: O(N) - where N is the number of nodes in the smaller tree
# Space Complexity: O(H) - where H is the height of the tree (call stack usage)
