class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initialize dictionaries to count character occurrences
        count1 = {}
        count2 = {}
        
        # Count characters in the first string
        for i in s:
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1
                
        # Count characters in the second string
        for j in t:
            if j in count2:
                count2[j] += 1
            else:
                count2[j] = 1
                
        # Compare the two dictionaries to determine if the strings are anagrams
        return count1 == count2

# Time Complexity: O(n)
# Space Complexity: O(n)

# Explanation:
# Time Complexity: O(n), where n is the length of the longer string.
# We traverse each string once to count character occurrences, leading to a linear time complexity.

# Space Complexity: O(n) because in the worst case, we store up to n unique characters
# (where n is the length of the strings) in the dictionaries.
