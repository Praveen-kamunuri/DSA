from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Returns the number of steps in the shortest transformation sequence from beginWord to endWord.
        Each step must change exactly one letter, and the new word must be in the wordList...
        """

        # If the endWord is not in the wordList, there's no valid path
        if endWord not in wordList:
            return 0

        # Initialize BFS queue with the starting word and step count
        q = deque()
        q.append((beginWord, 1))

        # Convert wordList to a set for faster lookup
        wordSet = set(wordList)

        # We use discard instead of remove to avoid KeyError
        # discard removes the word if it's present; otherwise does nothing
        wordSet.discard(beginWord)  # use remove(beginWord) if you're sure it's always in the list

        while q:
            word, steps = q.popleft()

            # If we've reached the endWord, return the number of steps
            if word == endWord:
                return steps

            # Try all possible one-letter transformations
            for i in range(len(word)):
                for c in range(ord('a'), ord('z') + 1):
                    next_word = word[:i] + chr(c) + word[i+1:]

                    # If the transformed word is in the set, it's a valid next step
                    if next_word in wordSet:
                        wordSet.remove(next_word)  # remove ensures we don't visit again
                        q.append((next_word, steps + 1))

        # If we exhaust the queue without finding endWord, return 0..
        return 0


"""
Time Complexity: O(N * L * 26)
    - N = total words in wordList
    - L = length of each word
    - For each position in each word (L), we try 26 letters, and lookup in set is O(1)

Space Complexity: O(N)
    - We store the wordList as a set (O(N))
    - The queue (BFS) can hold up to N elements in the worst case
"""
