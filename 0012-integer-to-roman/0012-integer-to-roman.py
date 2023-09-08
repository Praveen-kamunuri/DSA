class Solution(object):
    def intToRoman(self, num):
        # Define arrays for Roman numeral values and symbols
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        i = 0  # Initialize a counter to loop through val and sym arrays
        ans = ""  # Initialize an empty string to store the Roman numeral
        
        # Main loop to convert num to Roman numeral
        while num > 0:
            while num >= val[i]:
                ans += sym[i]  # Append the current symbol to the result string
                num -= val[i]  # Subtract the corresponding value from num
            i += 1  # Move to the next symbol and value in the arrays
        
        return ans  # Return the Roman numeral representation of num
