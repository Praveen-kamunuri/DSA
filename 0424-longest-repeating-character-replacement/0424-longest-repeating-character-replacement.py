class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0  # Initialize left pointer
        r = 0  # Initialize right pointer
        hash_arr = [0] * 26  # Frequency array for 26 letters (A-Z)
        max_freq = 0  # Keep track of the maximum frequency of any single character in the window
        n = len(s)  # Length of the input string
        max_len = 0  # The maximum length of the valid window

        # Sliding window approach
        while r < n:
            # Update the frequency of the current character (s[r])
            hash_arr[ord(s[r]) - ord('A')] += 1
            
            # Update the max_freq in the current window
            max_freq = max(max_freq, hash_arr[ord(s[r]) - ord('A')])
            
            # Check if the window size minus the max frequency character count exceeds the allowed k replacements
            while (r - l + 1) - max_freq > k:
                # Shrink the window by reducing the count of the leftmost character and moving left pointer
                hash_arr[ord(s[l]) - ord('A')] -= 1
                
                # Recalculate max_freq by iterating over the frequency array (constant time operation)
                max_freq = 0  # Reset max_freq
                for i in hash_arr:
                    max_freq = max(max_freq, i)  # Find the maximum frequency of any character in the window
                
                # Move the left pointer to shrink the window
                l += 1
            
            # Update the maximum length of a valid window that satisfies the condition
            max_len = max(max_len, r - l + 1)
            
            # Move the right pointer to expand the window
            r += 1
        
        # Return the maximum length of the substring after replacements
        return max_len

# Time Complexity (TC): O(n) 
# - We traverse the string with two pointers, and both pointers move at most n times, where n is the length of the string.
# - max_freq recalculations inside the inner loop are done in constant time (O(26)).

# Space Complexity (SC): O(1)
# - The space used is constant because we only use an array of size 26 (hash_arr) and a few variables.
