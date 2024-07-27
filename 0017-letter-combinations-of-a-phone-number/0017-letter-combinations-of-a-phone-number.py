from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, return an empty list
        if not digits:
            return []

        # Backtracking function to generate combinations
        def backtrack(ind, ds):
            # If the current index equals the length of digits, a combination is complete
            if ind == n:
                res.append(''.join(ds))  # Add the combination to the results
                return
            
            # Get the current digit and its corresponding letters
            curr_digit = digits[ind]
            letters = hashmap[curr_digit]
            
            # Iterate through the letters and recurse
            for letter in letters:
                ds.append(letter)  # Add the current letter to the combination
                backtrack(ind + 1, ds)  # Recurse to the next digit
                ds.pop()  # Backtrack, remove the last letter added

        # Mapping of digits to corresponding letters
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        n = len(digits)  # Length of the input digits
        res = []  # List to store the result combinations
        ds = []  # Temporary list to store current combination

        # Start the backtracking process
        backtrack(0, ds)
        
        return res

# Time Complexity (TC): O(4^n * n)
# Space Complexity (SC): O(n + 4^n * n)
