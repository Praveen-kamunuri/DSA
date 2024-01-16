class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        for i in range(2 ** n):
            ds = []
            for j in range(n):
                if i & (1 << j):
                    ds.append(nums[j])
            res.append(ds)
        return res
            
                    
        