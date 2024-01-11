from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        ds = []
        n = len(nums)
        
        def findSubset(ind):
            ans.append(ds[:])
            for i in range(ind , n):
                if i != ind and nums[i] == nums[i-1]:
                    continue

                ds.append(nums[i])
                findSubset(i + 1)
                ds.pop()
            
        nums.sort()
        findSubset(0)
        return ans