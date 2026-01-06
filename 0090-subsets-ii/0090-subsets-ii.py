

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array to handle duplicates
        nums.sort()
        ans = []  # List to store the final subsets
        ds = []   # List to temporarily store subsets during recursion
        n = len(nums)
        
        # Recursive function to find subsets
        def findSubset(ind):
            # Append the current subset to the result..
            ans.append(ds[:])
            
            # Iterate through the array from the current index
            for i in range(ind, n):
                # Skip duplicates to avoid duplicate subsets
                if i != ind and nums[i] == nums[i-1]:
                    continue

                # Include the current element in the subset
                ds.append(nums[i])
                
                # Recursive call with the next index
                findSubset(i + 1)
                
                # Backtrack: remove the last element to explore other possibilities
                ds.pop()
            
        
        # Start the recursion from index 0...
        findSubset(0)
        
        return ans