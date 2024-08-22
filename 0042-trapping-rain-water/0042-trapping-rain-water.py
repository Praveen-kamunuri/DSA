class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # Edge case
        if n <= 2:
            return 0
        
        # Arrays to store the maximum height to the left and right of each bar
        # Space complexity: O(n) for both left_max and right_max arrays
        left_max = [0] * n
        right_max = [0] * n
        
        # Initialize the left max array
        left_max[0] = height[0]
        for i in range(1, n):
            # Time complexity: O(n) for this loop
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Initialize the right max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            # Time complexity: O(n) for this loop
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate the trapped water
        total_water = 0
        for i in range(n):
            # Time complexity: O(n) for this loop
            trapped_water = min(left_max[i], right_max[i]) - height[i]
            if trapped_water > 0:
                total_water += trapped_water
        
        # Overall Time Complexity: O(n)
        # Overall Space Complexity: O(n)
        return total_water
