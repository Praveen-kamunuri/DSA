class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        
        k = k % n
        
        if k == 0:
            return

        start_ind = n - k
        li = []
        
        for i in range(start_ind, n):
            li.append(nums[i])

        for i in range(start_ind):
            li.append(nums[i])

        # Update the original 'nums' list with the rotated elements
        for i in range(n):
            nums[i] = li[i]
