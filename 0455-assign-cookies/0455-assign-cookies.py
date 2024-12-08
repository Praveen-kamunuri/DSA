class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """
        Problem:
        Given two arrays, g (greed factors of children) and s (sizes of cookies), 
        find the maximum number of children that can be content.

        Approach:
        Use a greedy algorithm to assign the smallest possible cookie to each child.
        """

        # Length of greed factors and cookie sizes arrays
        n = len(g)
        m = len(s)

        # Sort both arrays in ascending order to facilitate the greedy approach
        g.sort()  # Sort greed factors of children
        s.sort()  # Sort cookie sizes

        # Initialize pointers for greed factors (right) and cookie sizes (left)
        left = 0
        right = 0

        # Greedy allocation of cookies
        while left < m and right < n:
            # If the current cookie satisfies the current child's greed factor
            if g[right] <= s[left]:
                right += 1  # Move to the next child (content child)

            left += 1  # Move to the next cookie regardless

        # The number of content children is stored in 'right'
        return right

        """
        Time Complexity:
        - Sorting g and s: O(n log n + m log m), where n and m are the lengths of g and s.
        - Iterating through g and s: O(max(n, m)).
        - Overall: O(n log n + m log m).

        Space Complexity:
        - Sorting is done in place, so no extra space is used.
        - Overall: O(1).
        """
