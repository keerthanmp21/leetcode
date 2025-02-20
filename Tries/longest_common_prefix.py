from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie1:
    def __init__(self):
        self.root = TrieNode()
        self.res = ""

    def insert(self, word, N):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur.children[c][1] += 1
            else:
                cur.children[c] = [TrieNode(), 1] 
            if cur.children[c][1] == N:
                self.res += c
            cur = cur.children[c][0]

class Trie2:
    def __init__(self):
        self.children = {}
        self.res = ""

    def insert(self, word, N):
        cur = self.children
        for c in word:
            if c in cur:
                cur[c][1] += 1
            else:
                cur[c] = [{}, 1] 
            if cur[c][1] == N:
                self.res += c
            cur = cur[c][0]

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.res = ""

    def insert(self, word, N):
        cur = self.children
        for c in word:
            ind = ord(c) - ord('a')
            if c in cur:
                cur[ind][1] += 1
            else:
                cur[ind] = [[None] * 26, 1] 
            
            if cur[ind][1] == N:
                self.res += c
            cur = cur[ind][0]

class Trie:
    def __init__(self):
        self.children = {}
        self.res = ""

    def insert(self, word, N):
        cur = self.children
        for c in word:
            if c in cur:
                cur[c][1] += 1
            else:
                cur[c] = [{}, 1] 
            if cur[c][1] == N:
                self.res += c
            cur = cur[c][0]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        if N == 0:
            return ""

        trie = Trie()
        for word in strs:
            if word == "":
                return ""
            trie.insert(word, N)

        return trie.res
       
'''
To analyze the time and space complexity of the provided Trie implementation for 
finding the longest common prefix, let's break it down step-by-step.

### Time Complexity

1. **Insertion of Each Word**:
   - Each word in the input list `strs` is inserted into the Trie. Let's denote:
     - \( L \) as the maximum length of the words in `strs`.
     - \( N \) as the number of words in `strs`.

   - Inserting a single word of length \( L \) into the Trie takes \( O(L) \) time 
   because we need to traverse through each character of the word.
   - Therefore, inserting all \( N \) words takes \( O(N \cdot L) \).

2. **Checking for Common Prefix**:
   - During the insertion, you also check the count of children nodes. This involves 
   constant-time checks and updates per character, so this does not add additional 
   complexity.

Overall, the time complexity for inserting all words into the Trie is:
\[ O(N \cdot L) \]

### Space Complexity

1. **Space for Trie Nodes**:
   - The space required for the Trie depends on the number of unique characters across
     all inserted words.
   - In the worst case, if all characters are unique, the space complexity can be 
   \( O(N \cdot L) \) because each character in each word could create a new Trie node.

2. **Result Storage**:
   - The space used to store the result (the longest common prefix) will also be at 
   most \( O(L) \) since the longest common prefix can be as long as the length of the 
   longest word.

Overall, the space complexity for the Trie is:
\[ O(N \cdot L) \]

### Summary

- **Time Complexity**: \( O(N \cdot L) \)
- **Space Complexity**: \( O(N \cdot L) \)

This analysis shows that the solution is efficient in terms of both time and space for 
the problem of finding the longest common prefix using a Trie data structure.
'''