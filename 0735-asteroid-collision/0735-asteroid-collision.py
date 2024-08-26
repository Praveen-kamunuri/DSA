class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # Get the number of asteroids
        n = len(asteroids)
        
        # Initialize an empty stack to keep track of remaining asteroids
        stack = []
        
        # Iterate through all asteroids
        for i in range(n):
            # If the asteroid is moving to the right (positive), add it to the stack
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            
            # If the asteroid is moving to the left (negative)
            else:
                # While the stack has right-moving asteroids and the current left-moving asteroid 
                # is larger in absolute value (i.e., will destroy the right-moving ones)
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()  # Pop the right-moving asteroid as it's destroyed
                
                # If the top of the stack asteroid has the same magnitude but different direction
                if stack and stack[-1] == abs(asteroids[i]):
                    stack.pop()  # Both asteroids are destroyed
                
                # If no collision or the stack's top asteroid is moving left, push the current asteroid
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
                    
        # Return the remaining asteroids after all collisions
        return stack

# Time Complexity (TC):
# The outer loop runs through all asteroids once (O(n)). 
# Each asteroid is added to the stack at most once and removed from the stack at most once (O(1) per operation).
# Therefore, the total time complexity is O(n).

# Space Complexity (SC):
# The space complexity is O(n), where n is the number of asteroids, due to the usage of the stack to store the asteroids.
