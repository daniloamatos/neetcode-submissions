class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        maximum = 0
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            if len(seen) > maximum:
                maximum = len(seen)
            r+=1
        return maximum