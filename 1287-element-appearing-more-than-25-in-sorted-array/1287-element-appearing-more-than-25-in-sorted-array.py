from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Initialize a hashmap to store the count of each element in the array
        hashmap = {}
        
        # Count occurrences of each element in the array
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        # Calculate the minimum count required for an element to be considered "special"
        element_with_percentage = (1 / 4) * len(arr)
        
        # Iterate through the hashmap to find the "special" element
        for key, val in hashmap.items():
            if val > element_with_percentage:
                # Return the first "special" element found
                return key
