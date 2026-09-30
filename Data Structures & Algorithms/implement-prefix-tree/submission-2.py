class PrefixTree:

    def __init__(self):
        self.pre = defaultdict(bool)

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            if not self.pre.get(word[:i]): self.pre[word[:i]] = False
            self.pre[word] = True

    def search(self, word: str) -> bool:
        return self.pre.get(word, False)

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.pre
        