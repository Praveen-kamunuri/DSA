class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else: 
            num_str = str(x)
            n = len(num_str)
            start = 0
            end = n - 1
            while start <= end:
                if num_str[start] != num_str[end]:
                    return False
                start += 1
                end -= 1
            return True
        