from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get number of rows and columns in the image
        rows = len(image)
        cols = len(image[0])

        # Get the starting color (target color to be replaced)
        target_color = image[sr][sc]

        # If the starting pixel already has the new color, no changes are needed
        if target_color == color:
            return image

        # Initialize queue for BFS and add the starting pixel
        q = deque()
        q.append((sr, sc))

        while q:
            # Pop the front of the queue
            x, y = q.popleft()

            # If current pixel has the target color, change it to the new color
            if image[x][y] == target_color:
                image[x][y] = color

                # Check all 4-connected neighbors (up, down, left, right)
                directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # If the neighbor is in bounds and has the target color, add it to the queue
                    if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == target_color:
                        q.append((nx, ny))

        return image

# Time Complexity (TC): O(N), where N is the number of pixels in the image.
# In the worst case, we might need to visit every pixel once.

# Space Complexity (SC): O(N), for the queue used in BFS (in the worst case, nearly all pixels could be queued).
