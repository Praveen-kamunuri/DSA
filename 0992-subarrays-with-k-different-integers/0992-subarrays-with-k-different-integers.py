class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # Helper function to count subarrays with at most k distinct integers
        def solve(nums, k):
            l = 0  # left pointer of the sliding window
            r = 0  # right pointer of the sliding window
            cnt = 0  # count of subarrays with at most k distinct integers
            hashmap = {}  # stores the frequency of each number in the current window
            
            # Expand the window by moving the right pointer
            while r < len(nums):
                # Add the current element to the hashmap (increment frequency)
                if nums[r] in hashmap:
                    hashmap[nums[r]] += 1
                else:
                    hashmap[nums[r]] = 1
                
                # If the number of distinct elements in the window exceeds k,
                # shrink the window by moving the left pointer
                while len(hashmap) > k:
                    hashmap[nums[l]] -= 1  # decrease the frequency of the leftmost element
                    
                    # If its frequency becomes zero, remove it from the hashmap
                    if hashmap[nums[l]] == 0:
                        del hashmap[nums[l]]
                    
                    l += 1  # move the left pointer to the right
                
                # Add the number of subarrays ending at 'r' that have at most k distinct integers
                cnt += (r - l + 1)
                r += 1  # move the right pointer to the next element
                
            return cnt
        
        # The number of subarrays with exactly k distinct integers is the difference between
        # the number of subarrays with at most k distinct integers and at most k-1 distinct integers.
        return solve(nums, k) - solve(nums, k - 1)

# Time Complexity (TC):
# Both the helper function and the main function operate in O(n) time.
# This is because each element is processed at most twice (once when expanding the window with 'r'
# and once when shrinking the window with 'l'). So, the overall time complexity is O(n).

# Space Complexity (SC):
# The space complexity is O(k), where 'k' is the number of distinct integers allowed.
# This is due to the usage of the hashmap that stores the frequencies of at most 'k' distinct elements at any time.
