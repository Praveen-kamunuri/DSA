from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Define a recursive function to generate subsets
        def solve(ind, ans, ds):
            # Base case: if the current index is equal to the length of the input array,
            # append the current subset (deep copy of ds) to the answer list and return
            if ind == n:
                ans.append(ds[:])
                return
                
            # Include the current element at index 'ind' in the subset
            ds.append(nums[ind])
            solve(ind + 1, ans, ds)  # Recursively generate subsets with the current element included
            
            # Exclude the current element at index 'ind' from the subset
            ds.pop()
            solve(ind + 1, ans, ds)  # Recursively generate subsets with the current element excluded
            
        # Initialize variables
        n = len(nums)  # Length of the input array
        ans = []       # List to store subsets
        ds = []        # List to store current subset being generated
        
        # Start generating subsets from index 0
        solve(0, ans, ds)
        
        return ans  # Return the list of subsets
