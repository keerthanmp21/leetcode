class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.suggestions.append(word)
            cur.suggestions.sort()
            if len(cur.suggestions)>3:
                cur.suggestions.pop()

    def search(self, word, root):
        res = []
        for c in word:
            if root:
                root = root.children.get(c)
            res.append(root.suggestions if root else [])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.search(searchWord, trie.root)