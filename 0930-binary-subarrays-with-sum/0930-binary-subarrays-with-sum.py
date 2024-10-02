class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Helper function to calculate the number of subarrays
        # with sum less than or equal to 'k'
        def solve(nums, k):
            if k < 0:
                # If k is less than 0, no valid subarray exists, so return 0
                return 0
                
            n = len(nums)  # Length of the nums array
            l = 0  # Left pointer
            summ = 0  # To keep track of the current sum of the subarray
            cnt = 0  # To count the number of subarrays

            # Iterate through the array with the right pointer 'r'
            for r in range(n):
                summ += nums[r]  # Add the current element to the sum

                # If the current sum exceeds 'k', move the left pointer 'l' to the right
                # until the sum becomes less than or equal to 'k'
                while summ > k:
                    summ -= nums[l]
                    l += 1
                
                # Count the subarrays ending at 'r' and starting anywhere from 'l' to 'r'
                cnt += r - l + 1
            return cnt

        # The number of subarrays with exactly 'goal' sum is the difference between
        # the number of subarrays with sum <= goal and the number of subarrays with sum < goal.
        return solve(nums, goal) - solve(nums, goal - 1)

# Time complexity (TC): O(n)
# - We iterate through the array once, and the left pointer moves at most 'n' steps as well.
# - So, the time complexity is O(n).

# Space complexity (SC): O(1)
# - We use a constant amount of extra space (variables for sum, count, etc.), so the space complexity is O(1).
