from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Create a dictionary to store the count of occurrences for each element in the array
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        # Use a set to keep track of unique occurrence counts
        hashSet = set()
        
        # Flag to determine if there are any duplicate occurrence counts
        flag = True
        
        # Iterate through the counts in the hashmap
        for count in hashmap.values():
            # Check if the count is already in the hashSet
            if count in hashSet:
                # Set flag to False and break out of the loop if a duplicate is found
                flag = False
                break
            else:
                # Add the count to the hashSet if it's not already present
                hashSet.add(count)
        
        # Return the final result indicating whether there are unique occurrences
        return flag
