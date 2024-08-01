from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        
        # If the mountain array has less than 3 elements, no peaks can exist
        if n == 1 or n == 2:
            return []
        
        res = []
        
        # Iterate through the array from the second element to the second last element
        for i in range(1, n - 1):
            # Check if the current element is greater than both its neighbors
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                res.append(i)
        
        return res

        # Time Complexity (TC): O(n)
        # Space Complexity (SC): O(n)
