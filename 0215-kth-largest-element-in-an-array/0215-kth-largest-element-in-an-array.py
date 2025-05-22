import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = [-i for i in nums]

        heapq.heapify(max_heap)

        ele = None

        while k > 0:
            ele = heapq.heappop(max_heap)
            k -= 1
        return -ele
            


        