from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store the final combinations
        ans = []
        # List to store the current combination being explored
        ds = []

        # Function to recursively find combinations
        def findCombination(ind, target):
            # Base case: if index reaches the end of candidates
            if ind == len(candidates):
                # Check if the target is achieved, and if so, append the current combination to ans
                if target == 0:
                    ans.append(ds[:])
                return

            # Check if the current candidate can be a part of the combination
            if candidates[ind] <= target:
                # Include the current candidate in the combination
                ds.append(candidates[ind])
                # Recursively call the function with updated index and target
                findCombination(ind, target - candidates[ind])
                # Backtrack by removing the last added candidate to explore other possibilities
                ds.pop()

            # Move on to the next candidate
            findCombination(ind + 1, target)

        # Start the recursive search from the beginning
        findCombination(0, target)
        # Return the final list of combinations
        return ans
