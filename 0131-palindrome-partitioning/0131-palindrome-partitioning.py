class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # To store the final list of palindrome partitions
        path = []  # To store the current path (current partition)
        
        # Function to generate all partitions starting from index `ind`
        def generate(ind):
            # If we have reached the end of the string, add the current partition to the result
            if ind == len(s):
                res.append(path[:])  # Append a copy of the current path
                return
            
            # Try to partition the string starting from `ind` to `i`
            for i in range(ind, len(s)):
                # If the substring s[ind:i+1] is a palindrome, proceed
                if ispal(s, ind, i):
                    path.append(s[ind:i+1])  # Add this palindrome substring to the current path
                    generate(i + 1)  # Recur for the remaining substring
                    path.pop()  # Backtrack and remove the last added palindrome substring
        
        # Function to check if the substring s[start:end+1] is a palindrome
        def ispal(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False  # Not a palindrome
                start += 1
                end -= 1
            return True  # It is a palindrome
        
        generate(0)  # Start the recursive generation from index 0
        return res  # Return the final result
