from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # 1. BFS to build graph and find levels
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordSet:
                            new_layer[next_word] += [path + [next_word] for path in layer[word]]
            wordSet -= set(new_layer.keys())
            layer = new_layer

        return []