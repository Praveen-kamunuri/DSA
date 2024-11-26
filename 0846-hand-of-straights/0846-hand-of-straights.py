import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)
        
        if n % groupSize != 0:
            return False
        
        hashmap = {}
        
        for card in hand:
            if card in hashmap:
                hashmap[card] += 1
            else:
                hashmap[card] = 1
        
        min_heap = list(hashmap.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            start = min_heap[0]
            
            for card in range(start, start + groupSize):
                if card not in hashmap or hashmap[card] == 0:
                    return False
                
                hashmap[card] -= 1
            
                if hashmap[card] == 0:
                    if card != min_heap[0]:
                        return False
                    
                    heapq.heappop(min_heap)
        return True
        
        
        
        