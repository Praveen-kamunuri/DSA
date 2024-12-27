class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the number and its index
        num_dict = {}
        
        # Iterate over the array
        for i, num in enumerate(nums):
            # Calculate the complement that would sum to the target
            complement = target - num
            
            # If the complement exists in the dictionary, return the indices
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

# Example usage:
'''solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1'''