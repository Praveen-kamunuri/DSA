class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        
        # Iterate over each character in the input string
        for i in s:
            # If the character is an opening bracket, push it onto the stack
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            # If the character is a closing bracket
            else:
                # Check if the stack is empty; if it is, there's no matching opening bracket
                if not stack:
                    return False
                
                # Pop the top element from the stack, which should be the matching opening bracket
                ch = stack.pop()
                
                # Check if the popped opening bracket matches the current closing bracket
                if i == ')' and ch != '(':
                    return False
                elif i == ']' and ch != '[':
                    return False
                elif i == '}' and ch != '{':
                    return False
        
        # After processing all characters, check if the stack is empty
        # If the stack is empty, all opening brackets were matched correctly
        # If the stack is not empty, some opening brackets were not closed
        return len(stack) == 0