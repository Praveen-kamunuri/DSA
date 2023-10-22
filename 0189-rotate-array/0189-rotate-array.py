class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        
        k = k % n
        
        if k == 0:
            return nums
        
        start_ind = n - k
        li = []
        print("star",start_ind)
        for i in range(start_ind , n):
            li.append(nums[i])
        print("li",li)
            
        for i in range(start_ind):
            li.append(nums[i])
        print("ret",li)
        
        for i in range(n):
            nums[i] = li[i]
            
        return li
            
        
        