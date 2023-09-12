class Solution(object):
    def beautySum(self, s):
        n = len(s)
        result = 0

        for i in range(n):
            char_count = [0] * 26  # Initialize an array to store character frequencies (a to z)

            for j in range(i, n):
                char_count[ord(s[j]) - ord('a')] += 1  # Update character frequency
                
                # Calculate max and min frequency within the current substring
                max_freq = max(char_count)
                min_freq = min(freq for freq in char_count if freq > 0)

                # Calculate beauty for the current substring
                result += (max_freq - min_freq)

        return result
