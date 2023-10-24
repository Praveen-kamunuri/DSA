class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the numbers in the list and their indices
        hashmap = {}
        
        # Loop through the list, keeping track of both the number and its index
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement is in the hashmap and the indices are different
            if complement in hashmap and hashmap[complement] != i:
                # If a pair is found, return their indices
                return [hashmap[complement], i]
            
            # Add the current number and its index to the hashmap
            hashmap[num] = i
        
        # If no solution is found, return an empty list
        return []
