import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequencies of tasks
        freq = [0] * 26  # For tasks A-Z
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        # Step 2: Use a max heap for the frequencies
        max_heap = []
        for count in freq:
            if count > 0:
                heapq.heappush(max_heap, -count)  # Push negative for max heap
        
        time = 0
        cooldown = []  # List to store tasks in cooldown (remaining_count, cooldown_time)
        
        # Step 3: Simulate task execution
        while max_heap or cooldown:
            time += 1  # Increment time at each step
            
            if max_heap:
                current = heapq.heappop(max_heap)  # Get the task with the highest frequency
                if current + 1 < 0:  # If the task still has remaining count
                    cooldown.append((current + 1, time + n))  # Set cooldown time
            
            # Check if any tasks are ready to return to the heap
            if cooldown and cooldown[0][1] == time:  # If the first task's cooldown expires
                heapq.heappush(max_heap, cooldown.pop(0)[0])  # Push it back into the heap
        
        return time
