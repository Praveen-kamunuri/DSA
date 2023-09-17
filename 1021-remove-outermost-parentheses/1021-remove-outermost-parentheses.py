class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []  # Initialize an empty list to store the result.
        bal = 0   # Initialize a balance variable to keep track of parentheses balance.
        
        for i in s:
            if i == "(":
                if bal > 0:
                    res.append(i)  # Append '(' to the result if it's not the outermost '('.
                bal += 1  # Increment the balance for an open parenthesis '('.
            else:
                bal -= 1  # Decrement the balance for a closing parenthesis ')'.
                if bal > 0:
                    res.append(i)  # Append ')' to the result if it's not the outermost ')'.
        
        return "".join(res)  # Convert the result list to a string and return it.
