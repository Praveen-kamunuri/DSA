class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # Length of the number string
        n = len(num)
        
        # Initialize an empty string for the result (this will not be used directly until the end)
        res = ""
        
        # Stack to keep track of the digits in order to maintain the smallest possible number
        stack = []
        
        # Iterate over each character in the number string
        for char in num:
            # While the stack is not empty, k is greater than 0, and the top of the stack is greater than the current character
            # We pop from the stack to maintain a smaller number
            while stack and k > 0 and int(stack[-1]) > int(char):
                stack.pop()  # Remove the larger digit from the stack
                k -= 1  # Reduce k, since we've removed one digit
            stack.append(char)  # Add the current character to the stack
        
        # If there are still digits to remove (k > 0), remove from the end of the stack
        while k > 0:
            stack.pop()  # Pop the last remaining digits
            k -= 1  # Decrease k
        
        # If the stack is empty, return "0" because all digits have been removed
        if not stack:
            return "0"
        
        # Initialize an empty result string to build the final number
        res = ""
        
        # Pop all remaining elements in the stack and append them to the result string
        while stack:
            res += stack.pop()  # Append digits from stack in reverse order
        
        # Remove any leading zeros from the result (since it's in reverse order, these will be trailing zeros)
        while len(res) > 1 and res[-1] == '0':
            res = res[:-1]  # Remove the trailing zero
        
        # Since we built the result in reverse order, reverse it back to its correct form
        return res[::-1]  # Return the final result
    
# Time Complexity (TC):
# - The first loop runs for O(n) where n is the length of the input string `num`. 
# - In the worst case, each element could be pushed and popped once from the stack, 
#   so the while loop also takes O(n) time. 
# - Thus, the overall time complexity is O(n).

# Space Complexity (SC):
# - The space complexity is O(n) due to the space used by the stack to store the digits.
# - The result string `res` will also take O(n) space, but it's based on the stack.
# - Hence, the total space complexity is O(n).
