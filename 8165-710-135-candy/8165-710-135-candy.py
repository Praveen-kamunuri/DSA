class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        # Initialize the total candies to 1 for the first child
        summ = 1  
        
        i = 1  # Start iterating from the second child
        
        while i < n:
            # If the current rating is equal to the previous one, assign 1 candy
            if ratings[i] == ratings[i - 1]:
                summ += 1
                i += 1
                continue
            
            # Start counting the peak (increasing slope)
            peak = 1  
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1  # Increase the candy count for the peak
                summ += peak  # Add candies for this child
                i += 1  # Move to the next child
            
            # Start counting the valley (decreasing slope)
            down = 1  
            while i < n and ratings[i] < ratings[i - 1]:
                summ += down  # Add candies for this child
                i += 1  # Move to the next child
                down += 1  # Increase the candy count for the valley
            
            # If the valley (`down`) is longer than the peak, adjust total candies
            if down > peak:
                summ += down - peak  # Adjust the overlap of peak and valley
        
        return summ

# Time Complexity (TC):
# The algorithm iterates through the `ratings` list once, performing a single traversal of the array. 
# Both the ascending (peak) and descending (valley) slopes are processed in linear time.
# Hence, the overall time complexity is O(n), where n is the length of the `ratings` list.

# Space Complexity (SC):
# The algorithm uses a constant amount of extra space for variables (`summ`, `peak`, `down`, etc.).
# Therefore, the space complexity is O(1).

# Example Usage:
# ratings = [1, 0, 2]
# solution = Solution()
# print(solution.candy(ratings))  # Output: 5
