class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)  # Total number of cards
        
        l_sum = 0  # Sum of the first k cards from the left
        r_sum = 0  # Sum of the cards picked from the right (initialized to 0)
        max_sum = 0  # To store the maximum score
        
        # Calculate the sum of the first k cards from the left
        for i in range(k):
            l_sum += cardPoints[i]  # Add the current card value to the left sum
            max_sum = l_sum  # Initially, the max_sum is just the sum of the left k cards
        
        right_ind = n - 1  # Start index for picking cards from the right end
        
        # Start removing cards from the left and adding from the right
        for j in range(k-1, -1, -1):  # Loop through k cards in reverse from the left
            l_sum = l_sum - cardPoints[j]  # Subtract the current card from left sum
            r_sum = r_sum + cardPoints[right_ind]  # Add the current right card to right sum
            max_sum = max(max_sum, l_sum + r_sum)  # Update max_sum with the max of current sums
            right_ind -= 1  # Move the right pointer leftwards
        
        return max_sum  # Return the maximum sum achievable

# Time Complexity (TC):
# O(k) since we are processing at most k cards in both the left and right passes.
# The first loop runs k times and the second loop runs k times as well, making it O(k).

# Space Complexity (SC):
# O(1) as we are using only a few extra variables to store the sums and indices,
# and the input list is not modified or copied.
