class Solution(object):
    def sortColors(self, nums):
        cont0 = 0
        cont1 = 0
        cont2 = 0
        
        # Iterate over the input array to count the occurrences of each color
        for i in range(len(nums)):
            if nums[i] == 0:
                cont0 += 1
            elif nums[i] == 1:
                cont1 += 1
            elif nums[i] == 2:
                cont2 += 1
        
        # Update the input array to sort the colors
        for i in range(cont0):
            nums[i] = 0
        for i in range(cont0, cont0 + cont1):
            nums[i] = 1
        for i in range(cont0 + cont1, cont0 + cont1 + cont2):
            nums[i] = 2
        
        return nums
