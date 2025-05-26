class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = len(strs[0])

        for i in strs:
            if len(i) < min_len:
                min_len = len(i)

        prefix = ''
        for i in range(min_len):
            current_char = strs[0][i]

            for word in strs:
                if word[i] != current_char:
                    return prefix
            prefix += current_char
        return prefix

        