class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Get the length of the input list 'nums'
        n = len(nums)
        
        # Create a new list 'ans' with the same length, initialized with None values
        ans = [None] * n
        
        # Initialize two indices, one for positive numbers and one for negative numbers
        positive_ind = 0
        negative_ind = 1
        
        # Iterate through the elements in the 'nums' list
        for i in range(n):
            # If the current element is negative, place it in the 'ans' list at the negative index
            if nums[i] < 0:
                ans[negative_ind] = nums[i]
                # Increment the negative index by 2 to maintain the gap between negative numbers
                negative_ind += 2
            # If the current element is positive, place it in the 'ans' list at the positive index
            else:
                ans[positive_ind] = nums[i]
                # Increment the positive index by 2 to maintain the gap between positive numbers
                positive_ind += 2
        
        # Return the 'ans' list, which contains rearranged positive and negative numbers
        return ans
