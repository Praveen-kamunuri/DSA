class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Get the length of the input list `nums`
        n = len(nums)
        
        # Initialize a pointer `i` to 0, which keeps track of the unique elements
        i = 0
        
        # Iterate through the list starting from the second element (index 1)
        for j in range(1, n):
            # Check if the current element is different from the element at index `i`
            if nums[i] != nums[j]:
                # If it's different, increment `i` to represent a new unique element
                i += 1
                # Update the element at index `i` to be the current (unique) element
                nums[i] = nums[j]
        
        # `i` now represents the index of the last unique element, so the count of unique elements is `i + 1`
        return i + 1
