class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = set(nums1)
        
        nums1 = list(nums1)
        
        nums2 = set(nums2)
        
        nums2 = list(nums2)
        
        res = []
        
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res
                