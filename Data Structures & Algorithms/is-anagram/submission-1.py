class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cS, cT = {}, {}

        for i in range(len(s)):
            cS[s[i]] = 1 + cS.get(s[i], 0) 
            cT[t[i]] = 1 + cT.get(t[i], 0) 
        for c in cS:
            if cS[c] != cT.get(c,0) :
                return False

        return True
            
            
        