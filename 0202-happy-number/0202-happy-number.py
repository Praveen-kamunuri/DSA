class Solution:
    def isHappy(self, n: int) -> bool:
        
        # Use a set to track numbers we've seen to detect cycles
        sett = set()
        
        # Helper function to calculate the sum of the squares of the digits of num
        def func(num):
            res = 0
            while num != 0:
                rem = num % 10
                num = num // 10 
                res += rem ** 2
            return res
        
        # Loop until n becomes 1 or we detect a cycle
        while n != 1:
            n = func(n)
            
            # If we've seen this number before, there's a cycle and n is not happy
            if n in sett:
                return False
            
            # Add the number to the set to track it
            sett.add(n)
        
        # If we exit the loop because n is 1, it's a happy number
        return True

# Time Complexity (TC): O((log n)^2)
# Space Complexity (SC): O(k) where k is the number of unique sums encountered before a cycle is detected or the number becomes 1
