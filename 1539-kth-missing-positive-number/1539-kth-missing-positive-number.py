class Solution(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return k + high + 1

        