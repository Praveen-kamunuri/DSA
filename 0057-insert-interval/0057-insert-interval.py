from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into a list of non-overlapping intervals and merges overlapping intervals.

        Parameters:
        intervals (List[List[int]]): A list of sorted, non-overlapping intervals.
        newInterval (List[int]): The new interval to insert.

        Returns:
        List[List[int]]: The updated list of merged intervals
        """
        
        n = len(intervals)
        result = []  # Result list to store the merged intervals
        i = 0  # Pointer to traverse the intervals
        
        # Step 1: Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])  # No overlap, safe to add the interval
            i += 1
        
        # Step 2: Merge all intervals that overlap with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:  # Check if intervals overlap
            # Update the start and end of the new interval to include the overlapping interval
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged interval.
        result.append(newInterval)
        
        # Step 3: Add all remaining intervals that start after the new interval ends
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result


# Time Complexity:
# - Traversing the list of intervals: O(n), where `n` is the number of intervals.
# - Adding intervals to the result and merging overlapping intervals are O(n) operations.
# Total: O(n)

# Space Complexity:
# - The space used for the result list: O(n) (in the worst case, all intervals are added to the result).
# Total: O(n)
