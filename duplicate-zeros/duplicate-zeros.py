class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        temp = 0
        dup_arr = arr[:]
        arr[:] = [0] * n
        
        for i in range(n):
            if dup_arr[i] == 0:
                temp += 1
            else:
                ind = i + temp
                if ind < n:
                    arr[ind] = dup_arr[i]
                else:
                    break
        
        