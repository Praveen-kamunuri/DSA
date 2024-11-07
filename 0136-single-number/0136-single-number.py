from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the result variable to store the single number
        res = 0
        
        # Iterate through each number in the input list
        for n in nums:
            # XOR the current number with the result
            # XORing a number with itself cancels out the number, leaving 0
            # So, if the same number appears twice, it will cancel out and not affect the result
            # If a number appears only once, XORing it with 0 will result in that number
            res = res ^ n
        
        # After iterating through all numbers, 'res' will contain the single number
        return res
