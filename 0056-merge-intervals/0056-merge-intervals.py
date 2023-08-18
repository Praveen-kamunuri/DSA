class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        ans = []
        
        # Sort the intervals based on their start values
        intervals.sort()
        
        for i in range(n):
            # If the ans list is empty or there's a gap between intervals, add the current interval
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                # Merge overlapping intervals by updating the end value of the last interval
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
                
        return ans
