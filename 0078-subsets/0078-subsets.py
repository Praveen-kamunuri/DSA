from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)  # Get the length of the input list nums
        res = []       # Initialize an empty list to store subsets
        
        # Loop through all possible subsets using binary representation
        for i in range(2**n):
            subset = []  # Initialize an empty list to represent the current subset
            
            # Check each bit of i to determine which elements to include in the subset
            for j in range(0, n):
                if i & (1 << j):  # If the j-th bit of i is set (1), include nums[j] in the subset
                    subset.append(nums[j])
            
            res.append(subset)  # Add the generated subset to the result list
        
        return res  # Return the list of all subsets
