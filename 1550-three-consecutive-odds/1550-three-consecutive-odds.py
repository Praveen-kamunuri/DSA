from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0  # Counter to track consecutive odd numbers
        
        for i in arr:
            if i % 2 == 1:  # Check if the number is odd
                cnt += 1  # Increment the count of consecutive odds
                if cnt == 3:  # If we have found three consecutive odds
                    return True
            else:
                cnt = 0  # Reset the count if the number is even
        
        return False  # Return False if no three consecutive odds are found
