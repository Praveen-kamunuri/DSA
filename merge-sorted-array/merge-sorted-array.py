class Solution(object):
    def merge(self, nums1, m, nums2, n):
        start_ind = m  # Initialize a pointer for the start of the portion to merge in nums1
        end_ind = len(nums1) - 1  # Calculate the end index of the nums1 array
        j = 0  # Initialize a pointer for nums2

        # Iterate through nums1 and nums2
        while start_ind < len(nums1) and j != n:
            nums1[start_ind] = nums2[j]  # Append nums2 element to nums1
            start_ind += 1
            j += 1

        nums1.sort()  # Sort the merged nums1 array (this could be optimized)

        return nums1  # Return the merged and sorted nums1 array
