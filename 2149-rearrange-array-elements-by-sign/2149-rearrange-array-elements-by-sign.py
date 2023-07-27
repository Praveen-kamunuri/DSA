class Solution(object):
    def rearrangeArray(self, nums):
        # Create a hash map to group positive and negative elements
        hashmap = {'pos': [], 'neg': []}

        # Group positive and negative elements in the hash map
        for i in range(len(nums)):
            if nums[i] > 0:
                hashmap['pos'].append(nums[i])
            else:
                hashmap['neg'].append(nums[i])

        # Create an empty list to store the rearranged elements
        li = []

        # Get the lengths of the 'pos' and 'neg' lists
        pos_len = len(hashmap['pos'])
        neg_len = len(hashmap['neg'])

        # Determine the maximum length between 'pos' and 'neg'
        max_len = max(pos_len, neg_len)

        # Iterate through the range of max_len
        for i in range(max_len):
            # Append elements from 'pos' to the list 'li' if the index is within bounds
            if i < pos_len:
                li.append(hashmap['pos'][i])

            # Append elements from 'neg' to the list 'li' if the index is within bounds
            if i < neg_len:
                li.append(hashmap['neg'][i])

        # Return the rearranged list
        return li
