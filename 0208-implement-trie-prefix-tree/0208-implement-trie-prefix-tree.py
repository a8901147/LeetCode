class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children26:
                cur.children26[c] = Node()
            cur = cur.children26[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children26:
                return False
            cur = cur.children26[c]
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children26:
                return False
            cur = cur.children26[c]
        return True

class Node:
    def __init__(self):
        self.end_of_word = False
        self.children26 = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)