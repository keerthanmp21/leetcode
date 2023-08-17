from collections import defaultdict, deque
from typing import List

class Solution:
    # bfs
    # tc O(m*n) m = len(word), n = len(worddict)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj_dict = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                adj_dict[pattern].append(word)

        q = deque([beginWord])
        visited = set()
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for adj_word in adj_dict[pattern]:
                        if adj_word not in visited:
                            visited.add(adj_word)
                            q.append(adj_word)
            res += 1

        return 0
