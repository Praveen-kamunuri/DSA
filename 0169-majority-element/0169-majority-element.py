class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}  # Initialize an empty hashmap to store element counts
        target = len(nums) // 2  # Calculate the target count required for majority

        # Iterate over each element in the nums list
        for ele in nums:
            if ele in hashmap:  # If element already exists in hashmap
                hashmap[ele] += 1  # Increment its count by 1
            else:
                hashmap[ele] = 1  # Add the element to hashmap with count 1

        # Iterate over each key-value pair in the hashmap
        for ele, value in hashmap.items():
            if value > target:  # If the count is greater than or equal to the target
                return ele  # Return the majority element

