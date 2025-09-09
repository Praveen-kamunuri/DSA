class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def generate(n,op, cl, string):

            if n == op == cl:
                res.append(string)
                return

            if op < n:
                generate(n, op + 1, cl, string + '(')

            if cl < op:
                generate(n, op, cl + 1, string + ')')

        generate(n, 0, 0, '')

        return res



        