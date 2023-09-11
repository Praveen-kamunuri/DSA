class Solution(object):
    def rotateString(self, s, goal):
        if (len(s) != len(goal)):
            return False
        q1 = []
        for i in range(len(s)):
            q1.insert(0, s[i])

        q2 = []
        for i in range(len(goal)):
            q2.insert(0, goal[i])

        k = len(goal)
        while (k > 0):
            ch = q2[0]
            q2.pop(0)
            q2.append(ch)
            if (q2 == q1):
                return True

            k -= 1

        return False