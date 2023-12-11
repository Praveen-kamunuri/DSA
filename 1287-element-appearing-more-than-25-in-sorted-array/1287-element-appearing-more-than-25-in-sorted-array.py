class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        element_with_percentage = (1 / 4) * len(arr)
        for key , val in hashmap.items():
            if val > element_with_percentage:
                return key