from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Create a defaultdict with an initial value of 0
        hashmap = defaultdict(int)
        
        n = len(nums)
        cnt = 0
        pre_sum = 0

        # Initialize the count for prefix sum 0 to 1
        hashmap[0] = 1

        for i in range(n):
            # Calculate the current prefix sum
            pre_sum += nums[i]
            
            # Calculate the value to be removed from the prefix sum
            remove = pre_sum - k
            
            # Add the count of subarrays with the required sum
            cnt += hashmap[remove]
            
            # Update the count of the current prefix sum in the dictionary
            hashmap[pre_sum] += 1

        # Return the total count of subarrays with the sum of k
        return cnt
