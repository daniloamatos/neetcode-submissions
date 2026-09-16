class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        l, r = 0, 0
        window = {}
        need = {}
        have = 0
        shortest = len(s) + 1
        output = [-1,-1]

        for char in t:
            need[char] = need.get(char, 0) + 1

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and need[s[r]] >= window[s[r]]: 
                have += 1
            while have == len(t):
                curr = r - l + 1
                if curr < shortest:
                    output = [l, r + 1]
                    shortest = curr
                    
                if s[l] in need and need[s[l]] >= window[s[l]]:
                    have -= 1
                window[s[l]] -=1
                l+=1
            r+=1

        return s[output[0]:output[1]] if shortest != len(s) + 1 else ""