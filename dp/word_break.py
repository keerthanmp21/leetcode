from typing import List
from functools import lru_cache


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


class Solution:
    # backtrack
    # tc O(2^n)
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        N = len(s)

        def backtrack(start):
            if start == N:
                return True
            for end in range(start + 1, N + 1):
                word = s[start:end]
                if word in wordDictSet and backtrack(end):
                    return True
            return False

        return backtrack(0)

    # dp
    # tc O(n^2), sc O(n)
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        N = len(s)
        dp = [-1] * N

        def backtrack(start):
            if start == N:
                return True
            if dp[start] != -1:
                return dp[start]
            for end in range(start + 1, N + 1):
                word = s[start:end]
                if word in wordDictSet and backtrack(end):
                    dp[start] = 1
                    return dp[start]
            dp[start] = 0
            return dp[start]

        return backtrack(0)

    # same as above but using inbuilt decorator
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        N = len(s)

        @lru_cache(None)
        def backtrack(start):
            if start == N:
                return True
            for end in range(start + 1, N + 1):
                word = s[start:end]
                if word in wordDictSet and backtrack(end):
                    return True
            return False

        return backtrack(0)

    # dp tabulation
    # tc O(n^2), sc O(n)
    def wordBreak4(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        t = Trie()
        for word in wordDict:
            t.addWord(word)

        # Memoization dictionary
        memo = {}

        def canSegment(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            
            # Try all possible substrings from the current position
            for end in range(start + 1, len(s) + 1):
                if t.startsWith(s[start:end]):  # Check if this is a valid prefix
                    # If we find a word, try to segment the remaining part of the string
                    if s[start:end] in wordDict and canSegment(end):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False

        return canSegment(0)