from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Check if the input digits is empty
        if not digits:
            return []

        # Define a mapping of digits to letters
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        # Helper function to generate combinations using backtracking
        def backtrack(index, path):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                res.append(''.join(path))
                return

            # Get the letters corresponding to the current digit
            curr_letter = digits[index]
            letters = hashmap[curr_letter]

            # Iterate through the letters and explore combinations
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        # Initialize an empty list to store the result
        res = []

        # Start the backtracking process with initial values
        backtrack(0, [])

        # Return the final result
        return res
