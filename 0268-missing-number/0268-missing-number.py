class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Get the length of the input list `nums`
        n = len(nums)
        
        # Calculate the expected sum of numbers from 0 to n using the formula for the sum of an arithmetic series
        summ = n * (n+1) // 2
        
        # Initialize a variable `s` to keep track of the sum of elements in the list
        s = 0
        
        # Iterate through the elements in the list
        for i in nums:
            s += i  # Add each element to the sum
        
        # Calculate and return the missing number by subtracting the actual sum from the expected sum
        return summ - s
