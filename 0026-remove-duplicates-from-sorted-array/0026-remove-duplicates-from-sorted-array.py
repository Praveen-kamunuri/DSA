class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Get the length of the nums list
        n = len(nums)
        
        # Initialize pointer i, which will track the last unique element's index
        i = 0
        
        # Iterate through the array with pointer j starting from index 1
        for j in range(1, n):
            # If nums[i] is equal to nums[j], we skip the current element
            if nums[i] == nums[j]:
                continue
            else:
                # When a new unique element is found, move it to the next position in the list
                nums[i + 1] = nums[j]
                
                # Move i to the next index, marking the position for the next unique element
                i = i + 1
        
        # Return the length of the array with unique elements
        return i + 1

        # Time Complexity: O(n)
        # We traverse the array once, where n is the length of the input list.
        
        # Space Complexity: O(1)
        # We are modifying the list in place without using any extra space.
