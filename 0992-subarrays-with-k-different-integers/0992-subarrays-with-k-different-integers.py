class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def solve(nums, k):
            l = 0
            r = 0
            cnt = 0
            hashmap = {}
            while r < len(nums):
                if nums[r] in hashmap:
                    hashmap[nums[r]] += 1
                else:
                    hashmap[nums[r]] = 1
                while len(hashmap) > k:
                    
                    hashmap[nums[l]] -= 1
                    
                    
                    if hashmap[nums[l]] == 0:
                        del hashmap[nums[l]]

                    l += 1
                cnt = cnt + (r - l + 1)
                r += 1
                
            return cnt
        
        return solve(nums, k) - solve(nums, k - 1)

                