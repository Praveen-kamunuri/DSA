class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies the list of numbers in-place to produce the next lexicographical permutation.
        If no such permutation exists (i.e., it's the highest permutation), it rearranges to the lowest.
        """

        # Helper function to reverse a list in-place
        def rev(arr):
            left = 0
            right = len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr

        n = len(nums)
        ind = -1  # index where the descending order break happens

        # Step 1: Find the first element from the right which is smaller than its next element
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # Step 2: If the entire array is in descending order, reverse it to get the lowest permutation
        if ind == -1:
            nums[:] = rev(nums)
            return

        # Step 3: Find the smallest element greater than nums[ind] to the right of ind
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]  # swap
                break

        # Step 4: Reverse the part of the array after ind to get the next permutation
        nums[ind + 1:] = rev(nums[ind + 1:])


# ----------------------------------------------------
# ✅ Time Complexity: O(n)
# - One pass to find the break point (ind)
# - One pass to find the next greater element
# - One pass to reverse the suffix
# - All operations are linear in total

# ✅ Space Complexity: O(1)
# - All modifications are done in-place; no extra space used except a few variables

# Example usage:
# nums = [1, 2, 3]
# Solution().nextPermutation(nums)
# print(nums)  # Output: [1, 3, 2]
