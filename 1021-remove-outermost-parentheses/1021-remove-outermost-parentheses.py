class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        bal = 0
        for i in s:
            if i == "(":
                if bal > 0:
                    res.append(i)
                bal += 1
            else:
                bal -= 1
                if bal > 0:
                    res.append(i)
        return "".join(res)
        