class Solution:
    def intToRoman(self, num: int) -> str:
        # Arrays for values and symbols in descending order of value
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        i = 0  # Initialize index for val and sym arrays
        res = ''  # Initialize an empty string to store the resulting Roman numeral
        
        # Iterate through each value and symbol
        while num > 0:
            # Repeat adding symbols while num is greater than or equal to the current value
            while num >= val[i]:
                res += sym[i]  # Append the corresponding symbol to the result
                num -= val[i]  # Subtract the value from num
                
            i += 1  # Move to the next value and symbol pair
        
        return res

# Time complexity: O(1) - The while loop iterates a fixed number of times regardless of input size.
# Space complexity: O(1) - The extra space used does not grow with the input size, remains constant.
