class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedString = sorted(s)
        sortedString2 = sorted(t)

        if sortedString == sortedString2:
            return True
        else:
            return False
            
        