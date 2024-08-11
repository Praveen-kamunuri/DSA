class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s)  # Get the length of the string
        
        word_len = 0  # Variable to keep track of the length of the last word
        
        i = n - 1  # Start from the last character in the string
        
        # Iterate backwards through the string
        while i >= 0:
            
            # If the current character is a space
            if s[i] == ' ':
                # If we haven't started counting a word yet, just move to the next character
                if word_len == 0:
                    i -= 1
                # If we have started counting a word, return the length of that word
                else:
                    return word_len
            else:
                # If the current character is not a space, increment the word length
                word_len += 1
                i -= 1
                
        # If the loop ends, return the word length (for cases where the entire string is one word)
        return word_len
