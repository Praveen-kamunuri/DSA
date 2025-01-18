# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Defaultdict is used to store nodes at each (x, y) position
        # x is the vertical column, y is the level (depth) of the node
        nodes = defaultdict(lambda: defaultdict(list))
        
        # Helper function to perform DFS traversal
        def dfs(node, x, y):
            # Base case: if the node is None, return
            if not node:
                return
            
            # Add the current node's value to the map at the correct position
            # nodes[x][y] will store the node values at (x, y)
            nodes[x][y].append(node.val)

            # Recursively traverse the left and right children, adjusting the x and y values
            dfs(node.left, x - 1, y + 1)  # Move left: decrease x, increase y
            dfs(node.right, x + 1, y + 1)  # Move right: increase x, increase y

        # Start DFS traversal from the root, at position (0, 0)
        dfs(root, 0, 0)
        
        # Prepare the result list to store the vertical order traversal
        result = []

        # Iterate through the nodes dictionary in sorted order of x (vertical columns)
        for x in sorted(nodes.keys()):
            cols = []  # Temporary list to store nodes at this vertical column
            
            # Iterate through each level (y) at the current vertical column (x)
            for y in sorted(nodes[x].keys()):
                # For each level, sort the values and add them to the cols list
                cols.extend(sorted(nodes[x][y]))

            # Add the sorted columns to the final result list
            result.append(cols)

        # Return the result containing the vertical order traversal
        return result

# Time Complexity (TC):
# - The DFS traversal visits each node once, so the time complexity is O(N), where N is the number of nodes in the tree.
# - Sorting the nodes within each vertical column and level will take O(K * log K), where K is the number of nodes at a given (x, y) position, but this is dominated by the total number of nodes.

# Overall Time Complexity: O(N * log K), where N is the number of nodes and K is the average number of nodes at each vertical and level position.

# Space Complexity (SC):
# - We use a defaultdict to store nodes, which requires space for all the nodes in the tree. 
# - Additionally, we use recursion for DFS, which requires O(H) space where H is the height of the tree due to the recursive stack.

# Overall Space Complexity: O(N), where N is the number of nodes in the tree.
