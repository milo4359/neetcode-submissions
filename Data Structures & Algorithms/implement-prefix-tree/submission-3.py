
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:


    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            sub = word[:i+1]
            if sub not in node.children:
                node.children[sub] = TrieNode()
            node = node.children[sub]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if word[:i+1] not in node.children: return False
            node = node.children[word[:i+1]]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[:i+1] not in node.children: return False
            node = node.children[prefix[:i+1]]
        return True
        