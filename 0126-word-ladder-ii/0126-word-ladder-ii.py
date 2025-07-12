from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(set)
        level = {beginWord}
        found = False

        # BFS to build parent links
        while level and not found:
            next_level = set()
            for word in level:
                wordSet.discard(word)
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordSet:
                            if next_word == endWord:
                                found = True
                            next_level.add(next_word)
                            parents[next_word].add(word)
            level = next_level

        res = []

        # DFS to build all paths using parent map
        def dfs(word, path):
            if word == beginWord:
                res.append([beginWord] + path[::-1])
                return
            for parent in parents[word]:
                dfs(parent, path + [word])

        if found:
            dfs(endWord, [])

        return res
