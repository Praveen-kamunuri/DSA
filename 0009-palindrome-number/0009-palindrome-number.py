class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is negative; negative numbers can't be palindromes
        if x < 0:
            return False
        else:
            # Convert the integer to a string to easily compare its digits
            num_str = str(x)
            n = len(num_str)
            start = 0
            end = n - 1
            
            # Iterate through the string from both ends towards the center
            while start <= end:
                # If the digits at the current positions are not equal, it's not a palindrome
                if num_str[start] != num_str[end]:
                    return False
                
                # Move the pointers towards the center
                start += 1
                end -= 1
            
            # If the loop completes without returning False, the number is a palindrome
            return True
