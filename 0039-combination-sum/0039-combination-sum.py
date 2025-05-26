from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Define a recursive function to generate combinations
        def generate(n, ds, ans, target, ind, summ):
            # Base case: If the index is equal to the length of candidates
            if ind == n:
                # If the sum of current combination equals the target, add it to ans
                if summ == target:
                    ans.append(ds[:])  # Append a copy of the current combination to ans
                return
            
            # Recursive case: If the sum of current combination plus the current candidate
            # is less than or equal to the target, consider including the current candidate
            if summ + candidates[ind] <= target:
                ds.append(candidates[ind])  # Include the current candidate in the combination
                # Recur with the updated combination and sum
                generate(n, ds, ans, target, ind, summ + candidates[ind])
                ds.pop()  # Backtrack: Remove the last added candidate
                
            # Regardless of whether the current candidate is included or not, move to the next candidate
            generate(n, ds, ans, target, ind + 1, summ)
    
        n = len(candidates)  # Get the length of candidates list
        ds = []  # Initialize an empty list to store a combination
        ans = []  # Initialize an empty list to store all valid combinations
        
        # Call the recursive function to generate combinations
        generate(n, ds, ans, target, 0, 0)
        
        return ans  # Return the list of valid combinations
