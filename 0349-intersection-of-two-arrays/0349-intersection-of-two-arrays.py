
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert nums1 to a set
        set1 = set(nums1)
        
        # Convert nums2 to a set
        set2 = set(nums2)
        
        # Find intersection using set intersection operation
        res = set1 & set2
        
        # Convert set to list and return
        return list(res)



# Time Complexity (TC): O(n + m)
# Space Complexity (SC): O(n + m)
