class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = wordList[:]
        words.append(beginWord)
        graph = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                for word2 in words:
                    if word[:i] + word[i+1:] == word2[:i] + word2[i+1:]:
                        if word2 not in graph[word]: 
                            graph[word].append(word2)
                            graph[word2].append(word)
        
        visited = {beginWord}
        q = deque([beginWord])
        count = 1
        while q and endWord not in visited:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            count += 1
        return count if endWord in visited else 0
        

