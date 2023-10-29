class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string 's' into a list of words, using spaces as the delimiter
        words = s.split()
        
        # Reverse the order of the words in the list
        reversed_words = words[::-1]
        
        # Join the reversed words back together into a single string, using spaces as separators
        reversed_string = ' '.join(reversed_words)
        
        # Return the reversed string
        return reversed_string
