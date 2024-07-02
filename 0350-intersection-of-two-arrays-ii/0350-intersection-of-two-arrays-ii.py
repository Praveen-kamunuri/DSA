class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = {}
        
        
        res = []
        
        for i in nums1:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        for num in nums2:
            if num in hashmap and hashmap[num] > 0:
                res.append(num)
                
                hashmap[num] -= 1
        return res
                
        