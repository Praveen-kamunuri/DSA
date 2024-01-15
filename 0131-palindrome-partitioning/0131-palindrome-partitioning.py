from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # List to store the current partition
        ds = []
        # List to store all valid partitions
        res = []
        
        # Helper function to generate partitions
        def generate(ind):
            # If we reach the end of the string, add the current partition to the result
            if ind == len(s):
                res.append(ds[:])
                return
            
            # Iterate through the string starting from the current index
            for i in range(ind, len(s)):
                # Check if the substring from current index to i is a palindrome
                if isPal(s, ind, i):
                    # Add the palindrome to the current partition
                    ds.append(s[ind:i + 1])
                    # Recursively generate partitions for the remaining substring
                    generate(i + 1)
                    # Remove the last added element to backtrack and explore other possibilities
                    ds.pop()
                
        # Helper function to check if a substring is a palindrome
        def isPal(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True
        
        # Start generating partitions from the beginning of the string
        generate(0)
        # Return the final list of valid partitions
        return res
