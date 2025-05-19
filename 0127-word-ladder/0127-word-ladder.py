from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        q = deque()
        q.append((beginWord, 1))
        wordSet = set(wordList)
        wordSet.discard(beginWord)

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in range(ord('a'), ord('z') + 1):
                    next_word = word[:i] + chr(c) + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        q.append((next_word, steps + 1))
        return 0



        