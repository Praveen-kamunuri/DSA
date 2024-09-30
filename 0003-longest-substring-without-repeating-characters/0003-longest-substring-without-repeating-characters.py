class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_of_substr = 0
        s_list = list(s)
        current_substr = []
        print(s_list)
        max_len = 0
        for c in s_list: 
            print(c)
            if c not in current_substr: 
                current_substr.append(c)
                print(current_substr, len(current_substr))
            else: 
                if len(current_substr) > max_len: 
                    max_len = len(current_substr)
                index_of_dup = current_substr.index(c)
                current_substr = current_substr[index_of_dup+1:]
                current_substr.append(c)
                print(index_of_dup, current_substr)
        
        return max(max_len, len(current_substr))
        

            
        