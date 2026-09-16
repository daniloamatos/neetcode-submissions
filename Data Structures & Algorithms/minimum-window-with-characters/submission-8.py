class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        l, r = 0, 0
        window = defaultdict(int)
        need = defaultdict(int)
        have = 0
        shortest = len(s) + 1
        output = [-1,-1]

        for char in t:
            need[char] += 1

        while r < len(s):
            window[s[r]] += 1
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