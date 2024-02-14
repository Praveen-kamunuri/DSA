class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize a list to store the rearranged elements
        ans = [0] * n
        
        # Initialize two pointers to keep track of positions for positive and negative elements
        pos_ind = 0  # Pointer for positive indices
        neg_ind = 1  # Pointer for negative indices
        
        # Traverse through the input list
        for i in range(n):
            # If the current element is negative, place it at the next available negative index
            if nums[i] < 0:
                ans[neg_ind] = nums[i]
                neg_ind += 2  # Move the negative index pointer to the next available position
            # If the current element is positive, place it at the next available positive index
            else:
                ans[pos_ind] = nums[i]
                pos_ind += 2  # Move the positive index pointer to the next available position
        
        # Return the rearranged list
        return ans
