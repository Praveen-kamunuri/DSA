from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals by their ending times
        # This ensures that we always consider the interval that ends the earliest
        intervals.sort(key=lambda x: x[1])

        # Initialize the count of non-overlapping intervals
        count = 0
        # Track the end time of the last added interval to the non-overlapping set
        prev_end = float('-inf')

        # Iterate through the intervals
        for start, end in intervals:
            # If the current interval does not overlap with the last added interval
            if start >= prev_end:  # No overlap
                count += 1  # Increment the count of non-overlapping intervals
                prev_end = end  # Update the end time of the last added interval

        # Total intervals minus non-overlapping intervals gives the count of intervals to remove
        return len(intervals) - count

# Time Complexity: O(n log n)
# - Sorting the intervals takes O(n log n).
# - Iterating through the intervals takes O(n).
# Thus, the overall time complexity is O(n log n).

# Space Complexity: O(1)
# - The sorting operation is done in-place (if we consider Python's Timsort).
# - Only a few extra variables are used for counting and tracking the end time.
# Hence, the space complexity is O(1).