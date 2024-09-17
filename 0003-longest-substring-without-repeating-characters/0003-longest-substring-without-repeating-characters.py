class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)  # Get the length of the input string
        l = 0  # Left pointer, which tracks the start of the current window
        r = 0  # Right pointer, which expands the window to include new characters
        max_len = 0  # To store the length of the longest substring found so far
        hash_arr = [-1] * 255  # Array to store the last index of each character (using ASCII values as indices)
        
        # Iterate over the string with the right pointer
        while r < n:
            # If character s[r] has been seen before and is within the current window, move the left pointer
            if hash_arr[ord(s[r])] != -1:
                if hash_arr[ord(s[r])] >= l:
                    l = hash_arr[ord(s[r])] + 1  # Update left pointer to skip over the repeated character
            
            # Calculate the current window size
            curr_len = r - l + 1
            # Update max_len with the maximum between current window size and previous max_len
            max_len = max(curr_len, max_len)
            
            # Update the last seen index of character s[r]
            hash_arr[ord(s[r])] = r
            # Move the right pointer forward to check the next character
            r += 1
        
        # Return the maximum length of the substring without repeating characters
        return max_len

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1), since the size of the hash_arr is constant (255 elements regardless of input size)
