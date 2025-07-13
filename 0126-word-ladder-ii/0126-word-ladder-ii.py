from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Convert wordList to a set for O(1) lookup
        wordSet = set(wordList)
        
        # If endWord is not in the list, no transformation is possible..
        if endWord not in wordSet:
            return []

        # Dictionary to store all parent links for each word
        parents = defaultdict(set)

        # Level stores words at current BFS level
        level = {beginWord}

        # Flag to indicate if endWord is found during BFS
        found = False

        # BFS to construct the graph (track shortest paths)
        while level and not found:
            next_level = set()

            # Remove current level words from wordSet to avoid revisiting
            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        # Generate a new word by changing one letter at a time
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordSet:
                            if next_word == endWord:
                                found = True
                            next_level.add(next_word)
                            parents[next_word].add(word)
            
            # Move to next level
            level = next_level

        res = []

        # DFS to reconstruct paths from endWord to beginWord using parent links
        def dfs(word, path):
            if word == beginWord:
                # If we reached the start, add reversed path to results
                res.append([beginWord] + path[::-1])
                return
            for parent in parents[word]:
                dfs(parent, path + [word])

        # If we found the endWord, start DFS from it
        if found:
            dfs(endWord, [])

        return res



# \U0001f9e0 Time Complexity:
# BFS Traversal:

# Each word has up to 26 * L transformations (L = length of the word).

# For N words in wordList, total complexity is roughly O(N × L × 26) = O(N × L).

# DFS Traversal:

# Worst-case: if all words form valid paths, exponential in depth — O(P × L), where P = number of shortest paths found.

# Total: O(N × L + P × L)

# \U0001f9e0 Space Complexity:
# wordSet, parents, level, next_level: O(N)

# res: stores all paths, can be O(P × L)

# Call stack for DFS: O(L)

# Total: O(N + P × L)

