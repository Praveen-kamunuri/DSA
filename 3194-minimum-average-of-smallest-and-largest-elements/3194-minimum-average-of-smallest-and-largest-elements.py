from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        def findMin(arr):
            # Find the minimum value in the array
            mini = arr[0]
            for num in arr:
                if num < mini:
                    mini = num
            return mini

        nums.sort()  # Sort the input list
        # Sorting takes O(n log n) time
        
        res = []
        
        while nums:
            n = len(nums)
            if n == 1:
                # If there is only one element left, we take it as both the min and max
                mini = maxi = nums[0]
            else:
                # Otherwise, we take the first (min) and last (max) elements
                mini = nums[0]
                maxi = nums[-1]

            res.append((mini + maxi) / 2)
            
            nums = nums[1:-1]  # Remove the first and last elements
            # Removing elements takes O(n) time each iteration (as slicing a list creates a new list)
        
        ans = findMin(res)  # Find the minimum average
        # Finding minimum takes O(m) time where m is the length of res
        
        return float(ans)  # Return the minimum average as a float


# Time Complexity (TC):
# 1. Sorting: O(n log n)
# 2. Iterative Reduction: O(n^2) 
#    - List slicing in each iteration
# 3. Finding Minimum: O(n)
# Overall Time Complexity: O(n log n) + O(n^2) + O(n) = O(n^2)

# Space Complexity (SC):
# 1. Sorting: O(n) space due to TimSort algorithm
# 2. Result List: O(n) for storing the averages
# 3. Iterative Reduction: O(n) space for new lists created during slicing
# Overall Space Complexity: O(n)
