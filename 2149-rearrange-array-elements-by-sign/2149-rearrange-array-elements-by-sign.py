class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        ans = []
        
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        n = len(nums)
        
        for i in range(n//2):
            
            ans.append(pos[i])
            ans.append(neg[i])
            
        return ans
            
        