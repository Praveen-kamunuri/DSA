class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        ans = []
        nums.sort()  # Sort the input list
        
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates by continuing to the next iteration
            
            j = i + 1  # Start the second pointer at the element next to i
            k = n - 1  # Start the third pointer at the last element
            
            while j < k:
                trip_sum = nums[i] + nums[j] + nums[k]
                
                if trip_sum < 0:
                    j += 1  # Move the second pointer to the right
                elif trip_sum > 0:
                    k -= 1  # Move the third pointer to the left
                else:
                    # Found a valid triple, add it to the answer
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    
                    # Skip duplicates by incrementing the second pointer
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                        
                    # Skip duplicates by decrementing the third pointer
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        
        return ans
