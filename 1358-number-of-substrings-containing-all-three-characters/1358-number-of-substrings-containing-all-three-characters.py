class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        n = len(s)  # Length of the input string
        
        cnt = 0  # Initialize a counter to store the number of valid substrings
        
        # Array to keep track of the last seen index of 'a', 'b', and 'c'.
        # We map 'a' -> 0, 'b' -> 1, 'c' -> 2, so hash_arr will track the
        # indices for 'a', 'b', and 'c'.
        hash_arr = [-1] * 3  # [-1, -1, -1] initially, meaning none of 'a', 'b', 'c' are found yet.
        
        # Iterate through each character in the string
        for i in range(n):
            # Update the last seen index for the current character ('a', 'b', or 'c')
            hash_arr[ord(s[i]) - ord('a')] = i
            
            # Check if we have seen all three characters ('a', 'b', and 'c')
            if hash_arr[0] != -1 and hash_arr[1] != -1 and hash_arr[2] != -1:
                # If we have seen all three, the number of substrings ending at index 'i' that
                # include at least one 'a', 'b', and 'c' is determined by the minimum of the last
                # seen indices of 'a', 'b', and 'c' (plus 1 to account for 0-based indexing).
                cnt += min(hash_arr) + 1  # Add the count of valid substrings to 'cnt'
        
        return cnt  # Return the total count of valid substrings

# Time Complexity (TC): O(n), where n is the length of the input string `s`. 
# We only loop through the string once, performing constant time operations.

# Space Complexity (SC): O(1), constant space, as the only extra space used is the fixed-size array `hash_arr` of size 3.
