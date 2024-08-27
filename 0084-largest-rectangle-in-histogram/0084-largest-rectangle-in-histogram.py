class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Helper function to find the index of the previous smaller element for each element
        def find_prev_small(arr, n):
            res = [-1] * n  # Initialize the result array with -1 (no previous smaller element)
            stack = []  # Stack to store indices

            for i in range(n):
                # Maintain the stack for finding the previous smaller element
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()

                # If stack is not empty, the top of the stack is the previous smaller element
                if stack:
                    res[i] = stack[-1]

                # Push the current index to the stack
                stack.append(i)

            return res
        
        # Helper function to find the index of the next smaller element for each element
        def find_next_small(arr, n):
            res = [n] * n  # Initialize the result array with n (no next smaller element)
            stack = []  # Stack to store indices

            # Traverse the array in reverse to find next smaller elements
            for i in range(n - 1, -1, -1):
                # Maintain the stack for finding the next smaller element
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()

                # If stack is not empty, the top of the stack is the next smaller element
                if stack:
                    res[i] = stack[-1]

                # Push the current index to the stack
                stack.append(i)

            return res
        
        n = len(heights)  # Length of the heights array

        # Find the indices of the previous and next smaller elements
        prev_small_index = find_prev_small(heights, n)
        next_small_index = find_next_small(heights, n)

        maxi = 0  # Variable to store the maximum area

        # Calculate the maximum rectangle area for each bar in the histogram
        for i in range(n):
            # (next_small_index[i] - prev_small_index[i] - 1) gives the width of the rectangle
            # heights[i] is the height of the rectangle
            # Calculate the area and update maxi
            maxi = max(maxi, (next_small_index[i] - prev_small_index[i] - 1) * heights[i])

        return maxi

# Time Complexity (TC):
# - The `find_prev_small` function runs in O(n), where n is the number of bars in the histogram.
#   The stack operations are amortized O(1), so the total time complexity for this function is O(n).
# - The `find_next_small` function also runs in O(n) for the same reason.
# - The final loop that calculates the maximum rectangle area also runs in O(n).
# Therefore, the overall time complexity of the solution is O(n).

# Space Complexity (SC):
# - The space complexity is dominated by the space used for the result arrays `prev_small_index` and `next_small_index`, which both have size O(n).
# - The stack can also take up to O(n) space in the worst case.
# Therefore, the overall space complexity of the solution is O(n).
