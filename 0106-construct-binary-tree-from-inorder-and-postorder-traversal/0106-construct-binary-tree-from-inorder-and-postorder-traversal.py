# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case: If either inorder or postorder is empty, return None (no tree to build)
        if not inorder or not postorder:
            return None

        # The last element of postorder is always the root of the current subtree
        root_val = postorder.pop()

        # Create the root node
        root = TreeNode(root_val)

        # Find the index of root_val in inorder to determine left and right subtrees
        mid = inorder.index(root_val)

        # Recursively build the right subtree first (because postorder is processed from right to left)
        root.right = self.buildTree(inorder[mid + 1:], postorder)

        # Recursively build the left subtree
        root.left = self.buildTree(inorder[:mid], postorder)

        # Return the constructed tree
        return root

# Time Complexity (TC):
# - Finding the root in inorder takes O(N) in the worst case (using index()).
# - We make N recursive calls, one for each node.
# - Overall complexity: O(N^2) in the worst case (if the tree is skewed).
# - Can be improved to O(N) if we use a hashmap to store inorder indices.

# Space Complexity (SC):
# - The recursive call stack uses O(N) space in the worst case (skewed tree).
# - If the tree is balanced, the recursion depth is O(log N).
# - In the worst case, storing the inorder index in a hashmap reduces lookup time but requires O(N) space.
# - Overall worst-case space complexity: O(N).
