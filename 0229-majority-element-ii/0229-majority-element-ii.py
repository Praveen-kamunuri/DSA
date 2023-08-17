class Solution(object):
    def majorityElement(self, nums):
        # Calculate the length of the input list 'nums'
        n = len(nums)

        # Calculate the minimum count needed for an element to be considered a majority element
        mini = n // 3  # Using floor division to get an integer result

        # Create an empty dictionary to store element counts
        hashmap = {}

        # Create an empty list to store elements that appear more than 'mini' times
        result = []

        # Iterate through each element 'i' in the 'nums' list
        for i in nums:
            # Check if the element 'i' is already a key in the 'hashmap' dictionary
            if i in hashmap:
                # If it's a key, increment its count value by 1
                hashmap[i] += 1
            else:
                # If it's not a key, create a new key with value 1 in the 'hashmap' dictionary
                hashmap[i] = 1

            # Check if the count of the current element 'i' is greater than 'mini'
            # and if the element 'i' is not already in the 'result' list
            if hashmap[i] > mini and i not in result:
                # If both conditions are met, add the element 'i' to the 'result' list
                result.append(i)

        # Return the 'result' list containing elements that appear more than 'mini' times
        return result