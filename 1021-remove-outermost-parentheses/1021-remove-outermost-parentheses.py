class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        balance = 0
        for i in s:
            if i == '(':
                if balance > 0:
                    result.append(i)
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    result.append(i)
        return ''.join(result)
        