class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children26:
                cur.children26[c] = Node()
            cur = cur.children26[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(i,cur):
            for index in range(i,len(word)):
                c = word[index]
                if c == ".":
                    for child in cur.children26:
                        if dfs(index+1,cur.children26[child]):
                            return True
                    return False
                else:
                    if c in cur.children26:
                        cur = cur.children26[c]
                    else:
                        return False
            return cur.end_of_word

        return dfs(0,cur)
        
class Node:
    def __init__(self):
        self.children26 = {}
        self.end_of_word = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)