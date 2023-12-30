class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the final combinations
        ans = []
        # Initialize an empty list to store the current combination being formed
        ds = []

        # Define a recursive function to find combinations
        def findCombinations(ind, target):
            # Base case: If the index reaches the end of the candidates list
            if ind == len(candidates):
                # If the target is reduced to 0, add the current combination to the result
                if target == 0:
                    ans.append(ds[:])
                return

            # Check if the current candidate can be included in the combination
            if candidates[ind] <= target:
                # Include the current candidate in the combination
                ds.append(candidates[ind])
                # Recursively call the function with updated index and target
                findCombinations(ind, (target - candidates[ind]))
                # Remove the last element to backtrack and explore other possibilities
                ds.pop()

            # Move to the next candidate in the list
            findCombinations(ind + 1, target)

        # Start the recursive function with initial index and target
        findCombinations(0, target)
        # Return the final list of combinations
        return ans
