import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Use a min-heap to maintain the k largest elements
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.heap, val)
        # If the heap exceeds size k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # The root of the heap is the k-th largest element
        return self.heap[0]
    
    
    # Time Complexity (TC):
# 1. The `__init__` function processes `nums` and calls `add` for each element:
#    - Adding each element to the heap takes O(log k).
#    - For `n` elements in `nums`, it takes O(n log k).
# 2. The `add` method adds a value and ensures the heap size is k:
#    - Adding to the heap and potentially popping the smallest element takes O(log k).
# Overall, for `n` initialization elements and `m` calls to `add`, the time complexity is:
# O(n log k + m log k).

# Space Complexity (SC):
# 1. The heap size is maintained at k elements, requiring O(k) space.
# 2. No additional data structures with significant space are used.
# Overall space complexity: O(k).