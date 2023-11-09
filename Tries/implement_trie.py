class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if cur.children[ind] == None:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            ind = ord(c) - ord('a')
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)