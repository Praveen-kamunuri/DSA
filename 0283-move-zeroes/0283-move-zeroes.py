class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        # Check if the list contains only one element, and it's already a zero
        if n == 1 and nums[0] == 0:
            return
        
        j = -1
        # Find the index of the first zero in the list
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        # If no zero is found, return as there's nothing to move
        if j == -1:
            return
                
        # Iterate through the list starting from the index of the first zero (j)
        for i in range(j+1, n):
            # If a non-zero element is encountered, swap it with the first zero
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
