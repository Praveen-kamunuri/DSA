import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        hashmap = {}
        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1

        # Step 2: Add the frequencies to a max heap (negative values for max behavior)
        max_heap = []
        for freq in hashmap.values():
            heapq.heappush(max_heap, -freq)  # Push negative values for max heap

        time = 0  # Time counter
        cool_down_q = []  # To track tasks in their cooldown period

        # Step 3: Process tasks until both heap and cooldown queue are empty
        while max_heap or cool_down_q:
            time += 1  # Increment time at each step

            # Check if a task's cooldown has ended and add it back to the heap
            if cool_down_q and cool_down_q[0][0] == time:
                end_time, rem_freq = cool_down_q.pop(0)
                heapq.heappush(max_heap, rem_freq)

            # Process the most frequent task in the heap
            if max_heap:
                most_freq = heapq.heappop(max_heap)
                if most_freq < -1:  # If there's still work left for the task
                    rem_freq = most_freq + 1  # Decrease frequency
                    end_time = time + n + 1  # Calculate its next available time
                    cool_down_q.append((end_time, rem_freq))  # Add to cooldown queue

        return time  # Return total time required

# Complexity Analysis:
# Time Complexity (TC):
# 1. Counting task frequencies: O(t), where t = len(tasks).
# 2. Heap operations:
#    - Pushing frequencies: O(k * log(k)), where k = number of unique tasks.
#    - Total heap operations for processing tasks: O(t * log(k)).
# Final TC: O(t + t * log(k)), which simplifies to O(t * log(k)).

# Space Complexity (SC):
# 1. Hashmap storage: O(k), where k is the number of unique tasks.
# 2. Max heap storage: O(k) at its peak.
# 3. Cooldown queue storage: O(k) in the worst case (all tasks in cooldown).
# Final SC: O(k).