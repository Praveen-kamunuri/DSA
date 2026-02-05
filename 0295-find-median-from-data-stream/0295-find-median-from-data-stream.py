import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max-heap (negative values)
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        # Add to max-heap (small) with negation to simulate max-heap behavior
        heapq.heappush(self.small, -num)

        # Ensure the smallest value in large >= largest value in small
        if self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the sizes of the two heaps
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If odd total elements, return the top of the max-heap (small)
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If even total elements, return the average of the tops of both heaps...
        return (-self.small[0] + self.large[0]) / 2.0


# Time Complexity (TC):
# - `addNum`: O(log n) for maintaining heap properties (heap insertion/removal).
# - `findMedian`: O(1) as it only accesses the tops of heaps.

# Space Complexity (SC):
# - O(n) for storing elements in two heaps (`self.small` and `self.large`)..