class Solution(object):
    def merge(self, nums1, m, nums2, n):
        start_ind = m
        end_ind = len(nums1) - 1
        j = 0
        while start_ind < len(nums1) and j != n:
            nums1[start_ind] = nums2[j]
            start_ind += 1
            j += 1
        nums1.sort()
        return nums1
            
        