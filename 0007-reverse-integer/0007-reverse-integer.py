class Solution(object):
    def reverse(self, x):
        # Check if the number is negative
        if x < 0:
            sign = -1  # Set the sign to -1
            x = abs(x)  # Take the absolute value of x
        else:
            sign = 1  # Set the sign to 1 (positive or zero)

        num_str = str(x)  # Convert the number to a string
        l = ""  # Initialize an empty string to store the reversed digits

        # Iterate over the characters of num_str in reverse order
        for i in range(len(num_str) - 1, -1, -1):
            l = l + num_str[i]  # Concatenate the current character to l

        digit = int(l)  # Convert the reversed string back to an integer

        # Check if the reversed digit exceeds the maximum value of a signed 32-bit integer
        if digit > 2 ** 31 - 1:
            return 0  # Return 0 if it exceeds the range

        # Return the reversed value of x multiplied by the sign
        return sign * digit
