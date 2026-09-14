class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in s:
                if t.count(i) != s.count(i):
                    return False
            return True
        return False