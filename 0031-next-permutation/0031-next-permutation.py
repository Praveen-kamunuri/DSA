
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind = -1

        # Step 1: Find the first element from the right that is smaller than the next element.
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # Step 2: If no such element exists, reverse the entire list.
        if ind == -1:
            nums.reverse()
            return nums  # This line may not be needed as the list is reversed in-place.

        # Step 3: Find the smallest element to the right of `ind` that is greater than `nums[ind]`.
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                # Swap the two elements.
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 4: Reverse the subarray to the right of `ind`.
        nums[ind + 1:] = reversed(nums[ind + 1:])

        return nums  # Return the modified list.