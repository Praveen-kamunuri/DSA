class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(arr):
            n = len(arr)
            left = 0
            right = n - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr
        n = len(nums)
        ind = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break
            
        if ind == -1:
            nums[:] = rev(nums)
            return

        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        
        nums[ind+1:] = rev(nums[ind+1:])


        