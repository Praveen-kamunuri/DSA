class Solution(object):
    def rearrangeArray(self, nums):
        hashmap = {'pos':[] , 'neg':[]}
        for i in range(len(nums)):
            if nums[i] > 0:
                hashmap['pos'].append(nums[i])
            else:
                hashmap['neg'].append(nums[i])
        li = []
        pos_len = len(hashmap['pos'])
        neg_len = len(hashmap['neg'])
        max_len = max(pos_len , neg_len)
        for i in range(max_len):
            if i < max_len:
                li.append(hashmap['pos'][i])
            if i < max_len:
                li.append(hashmap['neg'][i])
        return li

            