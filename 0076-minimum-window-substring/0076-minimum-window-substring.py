class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize pointers and helper variables
        l = 0  # Left pointer
        r = 0  # Right pointer
        hash_arr = [0] * 256  # Hash array to store character counts for ASCII characters
        n = len(s)  # Length of string s
        m = len(t)  # Length of string t
        min_len = float('inf')  # To keep track of the minimum window length
        start_ind = -1  # To keep track of the starting index of the minimum window
        cnt = 0  # To count the number of characters matched
        
        # Populate hash_arr with the frequency of characters in t
        for i in t:
            hash_arr[ord(i)] += 1
    
        # Slide the right pointer to explore the window
        while r < n:
            # If the current character in s is in t (i.e., its count in hash_arr is positive)
            if hash_arr[ord(s[r])] > 0:
                cnt += 1  # Increment count of matched characters from t
            
            # Reduce the frequency of the current character in hash_arr
            hash_arr[ord(s[r])] -= 1
            
            # If all characters in t are matched (cnt == m)
            while cnt == m:
                # If the current window is smaller than the previously found window, update min_len
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start_ind = l  # Update the starting index of the current smallest window
                
                # Slide the left pointer to try minimizing the window
                hash_arr[ord(s[l])] += 1  # Revert the frequency change of the leftmost character
                if hash_arr[ord(s[l])] > 0:  # If removing this character affects the match
                    cnt -= 1  # Decrease the count of matched characters
                l += 1  # Move the left pointer to shrink the window
                
            # Move the right pointer to expand the window
            r += 1
        
        # If no valid window is found, return an empty string
        if start_ind == -1:
            return ""
        else:
            # Return the smallest window
            return s[start_ind:start_ind+min_len]

# Time Complexity (TC):
# - O(n), where n is the length of string s. The right pointer (r) and left pointer (l) each move through the string s at most once.
# - Updating and maintaining the hash_arr takes constant time, i.e., O(1), since it only deals with a fixed number of ASCII characters (256).

# Space Complexity (SC):
# - O(1) for the hash array of size 256, since it does not depend on the size of input strings.
# - Additional space is used for storing variables like l, r, min_len, start_ind, etc., but this is constant.
# - Thus, the overall space complexity is O(1) (constant space).
