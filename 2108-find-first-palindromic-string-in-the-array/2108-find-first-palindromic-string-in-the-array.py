class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        # Helper function to check if a string is a palindrome
        def ispal(string):
            n = len(string)
            i = 0
            j = n - 1
            
            while i <= j:
                if string[i] != string[j]:  # If characters at i and j don't match, it's not a palindrome
                    return False
                i += 1
                j -= 1
            
            return True
        
        # Main function to find the first palindrome in the list of words
        n = len(words)
        
        for i in range(n):
            if ispal(words[i]):  # Check if the current word is a palindrome
                return words[i]  # If it is, return the word
        return ""  # If no palindrome is found, return an empty string
