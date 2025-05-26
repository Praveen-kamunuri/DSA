from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Define a recursive function to generate combinations of parentheses
        def generate(n, ds, openn, close, string):
            # Base case: If the count of open and close parentheses reaches n,
            # append the generated string to the list of combinations
            if n == openn == close:
                ds.append(string)
                return
            
            # If the count of open parentheses is less than n, recursively call the function
            # with an additional open parenthesis
            if openn < n:
                generate(n, ds, openn + 1, close, string + '(')
            
            # If the count of close parentheses is less than the count of open parentheses,
            # recursively call the function with an additional close parenthesis
            if close < openn:
                generate(n, ds, openn, close + 1, string + ')')
                
        ds = []  # Initialize an empty list to store combinations
        
        # Call the recursive function to generate combinations
        generate(n, ds, 0, 0,'')
        
        return ds  # Return the list of generated combinations
