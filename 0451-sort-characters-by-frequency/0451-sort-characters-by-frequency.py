class Solution:
    def frequencySort(self, s: str) -> str:
        # Create an empty dictionary to store character frequencies
        hashmap = {}
        
        # Calculate character frequencies and store them in the hashmap
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        # Sort the keys (characters) based on their frequencies in decreasing order
        sorted_keys = sorted(hashmap.keys(), key=lambda k: hashmap[k], reverse=True)
        
        # Create a list of characters repeated based on their frequencies
        repeated_keys = [key * hashmap[key] for key in sorted_keys]
        
        # Concatenate the repeated characters to form the final result
        res = ''.join(repeated_keys)
        
        # Return the result as a string with characters sorted by frequency
        return res
