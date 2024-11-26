import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        # If total cards are not divisible by groupSize, it's impossible to divide
        if n % groupSize != 0:
            return False
        
        # Create a frequency hashmap to count occurrences of each card
        hashmap = {}
        for card in hand:
            if card in hashmap:
                hashmap[card] += 1
            else:
                hashmap[card] = 1
        
        # Convert the hashmap keys into a min-heap to process cards in sorted order
        min_heap = list(hashmap.keys())
        heapq.heapify(min_heap)
        
        # Process cards until the heap is empty
        while min_heap:
            start = min_heap[0]  # Smallest card to start the group
            
            # Try to form a group of size `groupSize`
            for card in range(start, start + groupSize):
                # If the card is missing or its count is zero, return False
                if card not in hashmap or hashmap[card] == 0:
                    return False
                
                # Decrement the count of the current card
                hashmap[card] -= 1
                
                # If the count becomes zero, check if it should be removed from the heap
                if hashmap[card] == 0:
                    if card != min_heap[0]:
                        return False  # The heap is out of order
                    heapq.heappop(min_heap)  # Remove the card from the heap
        
        return True

# Complexity Analysis:
# Time Complexity (TC):
# 1. Building the frequency hashmap: O(n), where n = len(hand).
# 2. Heapify operation: O(k * log(k)), where k is the number of unique cards.
# 3. While loop with card removal:
#    - Iterates over all cards (n) and does log(k) operations for heap operations.
#    - Total: O(n + k * log(k)).
# Final TC: O(n + k * log(k)).

# Space Complexity (SC):
# 1. Hashmap storage: O(k), where k is the number of unique cards.
# 2. Heap storage: O(k).
# Final SC: O(k).

# Example usage and outputs for validation:
solution = Solution()

# Test Case 1: Example from the prompt
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(solution.isNStraightHand(hand, groupSize))  # Output: True

# Test Case 2: Cannot form groups
hand = [1, 2, 3, 4, 5]
groupSize = 4
print(solution.isNStraightHand(hand, groupSize))  # Output: False

# Test Case 3: Handles duplicates properly
hand = [1, 1, 2, 2, 3, 3]
groupSize = 3
print(solution.isNStraightHand(hand, groupSize))  # Output: True

# Test Case 4: Missing cards to form a group
hand = [8, 10, 12]
groupSize = 3
print(solution.isNStraightHand(hand, groupSize))  # Output: False
