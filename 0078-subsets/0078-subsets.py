from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Define a recursive function to generate subsets
        def generate(n, ds, ans, ind):
            # Base case: If the index reaches the length of nums,
            # append the current subset to the answer and return
            if ind == n:
                ans.append(ds[:])  # Append a copy of ds to ans (as it will be modified in subsequent steps)
                return
        
            ds.append(nums[ind])  # Include the current element at index 'ind' in the subset
            generate(n, ds, ans, ind + 1)  # Recursive call to generate subsets including the current element
            ds.pop()  # Remove the current element to backtrack and generate subsets excluding the current element
            generate(n, ds, ans, ind + 1)  # Recursive call to generate subsets excluding the current element
        
        n = len(nums)  # Get the length of the input list nums
        ds = []  # Initialize an empty list to store subsets
        ans = []  # Initialize an empty list to store the final answer
        
        generate(n, ds, ans, 0)  # Call the recursive function to generate subsets, starting from index 0
        return ans  # Return the list of subsets
