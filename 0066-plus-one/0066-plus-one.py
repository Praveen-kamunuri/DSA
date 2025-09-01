class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Intuition:
        We're simulating the addition of 1 to a large integer represented as a list of digits.
        We start from the least significant digit (end of the list). 
        - If it's less than 9, we can safely add 1 and return.
        - If it's 9, we set it to 0 and continue carrying the 1 to the next digit.
        - If we carry all the way through (e.g., [9,9,9]), we insert a 1 at the beginning.
        """

        n = len(digits)

        # Iterate from the last digit to the first
        for i in range(n - 1, -1, -1):
            # If the digit is less than 9, simply increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, it becomes 0 and carry 1 to next digit
            digits[i] = 0

        # If we finish the loop, it means all digits were 9 (e.g., [9,9,9] -> [1,0,0,0])..
        return [1] + [0] * n


# Time Complexity: O(n) - we might need to iterate through all digits in the worst case
# Space Complexity: O(1) - constant extra space (excluding the output list, which is required)