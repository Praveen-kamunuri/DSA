class Solution:
    def beautySum(self, s: str) -> int:
        # Helper function to calculate the beauty of a string
        def freq(string):
            hashmap = {}
            for char in string:
                if char in hashmap:
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
            maxi = max(hashmap.values())
            mini = min(hashmap.values())
            return maxi - mini
        
        # Initialize the total sum of beauty
        total_sum = 0
        
        # Iterate through all possible substrings
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                sub_str = s[i:j+1]
                curr_freq = freq(sub_str)
                total_sum += curr_freq
        
        # Return the total sum of beauty
        return total_sum
