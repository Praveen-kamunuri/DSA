import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        max_heap = []
        
        hashmap = {}
        
        result = []
        
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for num, freq in hashmap.items():
            heapq.heappush(max_heap, (-freq, num))
            
        while max_heap and k != 0:
            freq, num = heapq.heappop(max_heap)
            
            result.append(num)
            
            k -= 1
        return result
        
        
        
         