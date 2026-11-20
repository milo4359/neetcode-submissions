class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        valid = {(0, 0)}

        for i in range(0, len(s3)):
            temp = set()
            for a, b in valid:
                if a < len(s1) and s1[a] == s3[i]: temp.add((a+1, b))
                if b < len(s2) and s2[b] == s3[i]: temp.add((a, b+1))
            if not temp: return False
            valid = temp

        return True 
