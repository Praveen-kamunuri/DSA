class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        # Calculate the bitwise XOR of start and goal
        ans = start ^ goal
        
        # Initialize a count variable to keep track of the number of bit flips needed
        count = 0
        
        # Iterate through each bit position from 0 to 30 (since integers are 32 bits in Python)
        for i in range(31):
            # Check if the ith bit of ans is set (i.e., 1)
            if ans & (1 << i):
                # If the bit is set, it means a flip is needed, so increment the count
                count += 1
        
        # Return the total count of bit flips needed
        return count
