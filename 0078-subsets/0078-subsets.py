class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []  # Initialize an empty list to store the subsets
        
        n = len(nums)  # Calculate the length of the input list
        
        for i in range(1 << n):  # Iterate through all possible subsets (2^n iterations)
            sub = []  # Initialize an empty list to store the current subset
            for j in range(n):  # Iterate through the elements of the input list
                # Check if the j-th bit of the binary representation of 'i' is set
                if (1 << j) & i:
                    sub.append(nums[j])  # If the bit is set, add the corresponding element to the subset
            ans.append(sub)  # Add the current subset to the list of subsets
        return ans  # Return the list of all subsets
