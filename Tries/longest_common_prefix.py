from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = ''
    def insert(self, word, length):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur.children[c][1] += 1
            else:
                cur.children[c] = [TrieNode(),1]
            if cur.children[c][1] == length:
                self.res += c
            cur = cur.children[c][0]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        length = len(strs)
        t = Trie()
        for word in strs:
            if word == '':
                return ''
            t.insert(word,length)
        return t.res