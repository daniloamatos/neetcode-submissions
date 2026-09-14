class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringsS = {}
        stringsT = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in stringsS:
                stringsS[s[i]] += 1
            else:
                stringsS[s[i]] = 1
            if t[i] in stringsT:
                stringsT[t[i]] += 1
            else:
                stringsT[t[i]] = 1

        return True if stringsT == stringsS else False