class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        prefix = 1  # Initialize prefix product
        suffix = 1  # Initialize suffix product
        ans = float('-inf')  # Initialize answer to negative infinity
        
        # Iterate through the array
        for i in range(n):
            # If prefix becomes 0, reset it to 1
            if prefix == 0:
                prefix = 1
            # If suffix becomes 0, reset it to 1
            if suffix == 0:
                suffix = 1
            # Update prefix and suffix products
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            # Update the answer with the maximum of current answer, prefix, and suffix
            ans = max(ans, max(prefix, suffix))
        
        return ans  # Return the maximum product found
