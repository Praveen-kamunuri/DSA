class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Get the length of the list
        n = len(s)
        
        # Initialize two pointers: start at the beginning, end at the last element
        start = 0
        end = n - 1 
        
        # Loop until the two pointers meet in the middle
        while start <= end:
            # Swap the elements at the start and end pointers
            s[start], s[end] = s[end], s[start]
            
            # Move the start pointer one step to the right
            start += 1
            # Move the end pointer one step to the left
            end -= 1



# Time Complexity (TC): O(n)
# The algorithm iterates through half of the list, so the time complexity is linear O(1) in relation to the
