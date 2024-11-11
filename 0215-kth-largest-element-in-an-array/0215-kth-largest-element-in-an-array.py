import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Step 1: Create a min-heap with the first k elements in nums
        # This takes O(k) space to store the heap of size k
        min_heap = nums[:k]  # Initialize the heap with the first k elements
        
        # Step 2: Convert the list into a min-heap in O(k) time
        heapq.heapify(min_heap)  # Heapify transforms it into a min-heap in O(k) time
        
        # Step 3: Process the remaining elements in nums (from index k to end)
        # Looping over the remaining (n - k) elements takes O(n - k) time
        for num in nums[k:]:
            # Check if the current number is larger than the smallest in the heap (min_heap[0])
            if num > min_heap[0]:  
                # Removing the smallest element takes O(log k) time
                heapq.heappop(min_heap)
                # Adding the current number takes O(log k) time
                heapq.heappush(min_heap, num)
        
        # Step 4: Return the smallest element in the min-heap, which is the kth largest element
        # This access is O(1) time
        return min_heap[0]

# Time Complexity (TC):
# - Building the initial heap takes O(k)
# - For the remaining (n - k) elements, each pop and push operation takes O(log k)
# - Total: O(k) + (n - k) * O(log k) = O(n log k)

# Space Complexity (SC):
# - The min-heap uses O(k) space to store the k largest elements
# - Total: O(k)
