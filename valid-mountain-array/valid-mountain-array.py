from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        # Check if array length is less than 3
        if n < 3:
            return False
        
        # Find the peak of the mountain
        peak_index = arr.index(max(arr))
        
        # Check if peak is at the start or end
        if peak_index == 0 or peak_index == n - 1:
            return False
        
        # Check if elements before peak are strictly increasing
        for i in range(1, peak_index):
            if arr[i] <= arr[i - 1]:
                return False
        
        # Check if elements after peak are strictly decreasing
        for i in range(peak_index + 1, n):
            if arr[i] >= arr[i - 1]:
                return False
        
        return True
