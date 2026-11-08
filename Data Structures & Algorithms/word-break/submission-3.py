class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        ends = [0]
        for end in ends:
            for i in range(end, len(s)):
                if s[end:i+1] in words and i + 1 not in ends:
                    ends.append(i+1)
        return True if len(s) in ends else False
            