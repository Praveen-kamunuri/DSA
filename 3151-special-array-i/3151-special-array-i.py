class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Helper function to check if two numbers have different parity
        def findParity(a, b):
            # Return True if one is even and the other is odd, else return False
            if (a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0):
                return True
            else:
                return False
        
        n = len(nums)  # Get the length of the input array
        
        # Iterate over the array from the first element to the second-to-last element
        for i in range(n - 1):
            # Check if the current element and the next element have different parity
            if findParity(nums[i], nums[i + 1]):
                continue  # If they do, continue to the next pair
            else:
                return False  # If they don't, return False immediately
        
        return True  # If all pairs have different parity, return True
