class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Get the number of bars in the histogram
        n = len(heights)
        
        # Stack to store indices of histogram bars
        stack = []
        
        # Variable to keep track of the maximum rectangle area found
        max_Area = 0
        
        # Iterate over each bar in the histogram
        for i in range(n):
            # Process the stack while the current bar is shorter than the bar at the top of the stack
            while stack and heights[stack[-1]] > heights[i]:
                # Pop the top element from the stack
                ele = heights[stack.pop()]
                # The current index is the Next Smaller Element (NSE) index
                nse = i
                # Determine the Previous Smaller Element (PSE) index
                pse = stack[-1] if stack else -1
                # Calculate the area with heights[ele] as the smallest bar
                max_Area = max(max_Area, ele * (nse - pse - 1))
            # Push the current bar's index onto the stack
            stack.append(i)
        
        # Process any remaining bars in the stack
        while stack:
            # NSE for the remaining bars is the end of the histogram (index n)
            nse = n
            # Pop the top element from the stack
            ele = heights[stack.pop()]
            # Determine the Previous Smaller Element (PSE) index
            pse = stack[-1] if stack else -1
            # Calculate the area for the popped bar
            max_Area = max(max_Area, ele * (nse - pse - 1))
        
        # Return the maximum area found
        return max_Area

# Time Complexity (TC): O(n)
# - Each bar is pushed onto the stack once and popped from the stack once.
# - The while loops ensure that each bar is processed in constant time (O(1)).
# - Thus, the overall time complexity is O(n), where n is the number of bars in the histogram.

# Space Complexity (SC): O(n)
# - The stack stores indices of histogram bars, which in the worst case can hold all n bars.
# - Therefore, the space complexity is O(n).
