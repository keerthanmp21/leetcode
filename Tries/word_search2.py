from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    # TLE
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        res = []
        for w in words:
            if self.exist(board, w):
                res.append(w)
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        N = len(word)
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, i):
            if i == N:
                return True
            if(r < 0 or r == ROWS or c < 0 or c == COLS or
            (r, c) in visited or board[r][c] != word[i]):
                return False

            visited.add((r, c))
            res = False
            for dr, dc in directions:
                res = res or dfs(r + dr, c + dc, i + 1)

            visited.remove((r, c))
            return res
            

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if(r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or board[r][c] not
              in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,'')
        
        return list(res)