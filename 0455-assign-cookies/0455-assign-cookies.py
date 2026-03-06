class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        child_len = len(g)

        size_len = len(s)

        g.sort()
        s.sort()

        left = 0
        right = 0

        while left < size_len and right < child_len:

            if g[right] <= s[left]:
                right += 1
            
            left += 1
        return right