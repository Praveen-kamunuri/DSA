from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # List to store the final combinations
        res = []
        # List to temporarily store combinations during recursion
        ds = []
        
        # Recursive function to find combinations
        def findComb(num, summ, size):
            # If the desired size is reached
            if size == k:
                # Check if the sum is equal to the target
                if summ == n:
                    res.append(ds[:])  # Append the current combination to the result
                return
            
            # Stop recursion if the number exceeds 9
            if num > 9:
                return
            
            # Include the current number in the combination
            ds.append(num)
            
            # Recursive call with the next number, updated sum, and increased size
            findComb(num + 1, summ + num, size + 1)
            
            # Backtrack: remove the last number to explore other possibilities
            ds.pop()
            
            # Recursive call without including the current number
            findComb(num + 1, summ, size)
            
        # Start the recursion with the initial parameters
        findComb(1, 0, 0)
        
        # Return the final list of combinations
        return res
