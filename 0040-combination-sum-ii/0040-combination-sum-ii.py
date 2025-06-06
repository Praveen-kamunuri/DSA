from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store the final combinations
        ans = []
        # List to store the current combination being explored
        ds = []
        # Sort the candidates to handle duplicates
        candidates.sort()
        
        # Recursive function to find combinations
        def findCombinations(ind, target):
            # If the target becomes 0, a valid combination is found
            if target == 0:
                ans.append(ds[:])  # Append a copy of the current combination to the result
                return
        
            # Iterate over the candidates starting from index 'ind'
            for i in range(ind, len(candidates)):
                # Skip duplicates to avoid duplicate combinations....
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                
                # If the current candidate is greater than the remaining target, break
                if candidates[i] > target:
                    break
                    
                # Include the current candidate in the combination
                ds.append(candidates[i])
                
                # Recursively call the function with the updated index and target
                findCombinations(i + 1, target - candidates[i])  # Use 'i' instead of 'ind'
                
                # Backtrack by removing the last added candidate to explore other possibilities
                ds.pop()
        
        # Start the backtracking process from index 0 with the given target
        findCombinations(0, target)
        
        # Return the final list of combinations
        return ans