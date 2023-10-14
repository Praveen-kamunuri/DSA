class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        n = len(nums)
        
        for i in range(1 << n):
            sub = []
            for j in range(n):
                
                
                if ( (1<<j) & i ):
                    sub.append(nums[j])
            ans.append(sub)
        return ans