class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Create an empty dictionary `hashmap` to store counts of each element
        hashmap = {}
        
        # Iterate through the elements in the input list `nums`
        for i in nums:
            if i in hashmap:
                # If the element exists in the dictionary, increment its count
                hashmap[i] += 1
            else:
                # If the element is not in the dictionary, add it with a count of 1
                hashmap[i] = 1
        
        # Iterate through key-value pairs in the `hashmap`
        for i, j in hashmap.items():
            # Check if the count of the element is 1, indicating it's the single number
            if hashmap[i] == 1:
                return i  # Return the single number
        
        # If no single number is found, return a default value (this may not be necessary)
        return None
