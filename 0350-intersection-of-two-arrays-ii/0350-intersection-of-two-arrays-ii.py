from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}  # Dictionary to count occurrences of each element in nums1
        res = []  # List to store the result (intersection elements)
        
        # Count the occurrences of each element in nums1
        for i in nums1:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        # Find the intersection elements with nums2
        for num in nums2:
            if num in hashmap and hashmap[num] > 0:
                res.append(num)  # Append the element to the result list
                hashmap[num] -= 1  # Decrease the count of the element in hashmap
        
        return res