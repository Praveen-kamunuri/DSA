import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Create a frequency map (hashmap) to store the count of each element
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1  # Increment count if element exists in hashmap
            else:
                hashmap[i] = 1   # Initialize count if element is new
        
        # Step 2: Use a max heap to store elements based on their frequency
        # We store negative frequencies because Python's heapq implements a min-heap
        max_heap = []
        for num, freq in hashmap.items():
            heapq.heappush(max_heap, (-freq, num))
        
        # Step 3: Extract the top k elements from the heap
        result = []
        while max_heap and k > 0:
            freq, num = heapq.heappop(max_heap)  # Pop the element with the highest frequency
            result.append(num)  # Add the number to the result
            k -= 1  # Decrement the counter for top k elements
        
        # Step 4: Return the result containing the top k frequent elements
        return result

# Example:
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# Output: [1, 2]

# Time Complexity:
# - Creating the hashmap: O(n), where n is the number of elements in nums
# - Building the heap: O(u log u), where u is the number of unique elements
# - Extracting k elements: O(k log u)
# Overall: O(n + u log u + k log u)

# Space Complexity:
# - Hashmap: O(u), for storing unique elements and their frequencies
# - Max heap: O(u), for storing up to u elements
# Overall: O(u)
