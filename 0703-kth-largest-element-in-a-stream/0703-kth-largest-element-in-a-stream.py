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