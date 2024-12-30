from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals by their starting points
        # Sorting ensures we can merge overlapping intervals in one pass.
        intervals.sort()
        
        n = len(intervals)  # Get the number of intervals
        
        ans = []  # This will store the merged intervals
        
        for i in range(n):
            # If the result list is empty or the current interval does not overlap with the last interval in ans
            if not ans or intervals[i][0] > ans[-1][1]:
                # Append the current interval to ans
                ans.append(intervals[i])
            else:
                # There is an overlap, merge the intervals by updating the end of the last interval
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        
        # Return the merged intervals
        return ans

# Time Complexity:
# Sorting the intervals takes O(n log n), where n is the number of intervals.
# The merging process involves a single pass through the intervals, which takes O(n).
# Overall time complexity: O(n log n).

# Space Complexity:
# The additional space used is for the `ans` list, which in the worst case (no intervals overlap),
# will contain all n intervals. Thus, the space complexity is O(n).
