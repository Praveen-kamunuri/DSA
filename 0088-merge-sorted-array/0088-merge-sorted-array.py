class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize the starting index for filling nums1 with nums2 elements
        start_ind = m
        # Calculate the ending index of the merged array
        end_ind = len(nums1) - 1
        # Initialize an index for iterating through nums2
        j = 0
        
        # Iterate through nums1 from the starting index to the end of the array,
        # and nums2 from the beginning to n, copying elements from nums2 to nums1
        while start_ind < len(nums1) and j != n:
            nums1[start_ind] = nums2[j]
            start_ind += 1
            j += 1
        
        # Sort the merged array (nums1)
        nums1.sort()
        
        return nums1
