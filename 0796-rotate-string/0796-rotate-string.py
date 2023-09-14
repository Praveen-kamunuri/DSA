class Solution(object):
    def rotateString(self, s, goal):
        # Check if the lengths of s and goal are not equal
        if len(s) != len(goal):
            return False
        
        # Check if s and goal are the same, indicating a valid rotation
        if s == goal:
            return True
        
        # Check if goal is a substring of s concatenated with itself
        if goal in s + s:
            return True
        else:
            # If none of the conditions are met, return False
            return False
