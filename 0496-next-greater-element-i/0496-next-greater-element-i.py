class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = {}
        
        stack = []
        
        res = []
        
        n = len(nums2)
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                next_greater[nums2[i]] = stack[-1]
            
            else:
                next_greater[nums2[i]] = -1
            
            stack.append(nums2[i])
                
            
        for num in nums1:
            res.append(next_greater[num])
        return res
    
                
            