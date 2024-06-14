class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Get the length of the input list
        n = len(nums)
        
        # Calculate the expected sum of the first n natural numbers using the formula n*(n+1)//2
        actual_sum = n * (n + 1) // 2
        
        # Initialize a variable to store the sum of the numbers in the input list
        summ = 0
        
        # Iterate through the input list and calculate the sum of its elements
        for i in range(n):
            summ += nums[i]
        
        # The missing number is the difference between the expected sum and the actual sum
        return (actual_sum - summ)
