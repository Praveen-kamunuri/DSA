class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(s, left, right):
            if left == 0 and right == 0:
                result.append(s)
                return
            if left > 0:
                generate(s + '(', left - 1, right)
            if right > left:
                generate(s + ')', left, right - 1)

        result = []
        generate('', n, n)
        return result
