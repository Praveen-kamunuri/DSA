# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def find_max_sum_path(node, maxi):

            if not node:
                return 0

            left = max(0, find_max_sum_path(node.left, maxi))

            right = max(0, find_max_sum_path(node.right, maxi))

            maxi[0] = max(maxi[0], left + right + node.val)

            return max(left, right) + node.val

        maxi = [float('-inf')]

        find_max_sum_path(root, maxi)
        
        return maxi[0]