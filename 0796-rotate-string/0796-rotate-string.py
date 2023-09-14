class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        
        if goal in s + s:
            return True
        else:
            False