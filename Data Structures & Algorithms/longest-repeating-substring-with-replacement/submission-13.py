class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0

        for target in set(s):
            invalid = deque()
            l = 0

            for r in range(len(s)):
                if s[r] != target:
                    invalid.append(r)

                if len(invalid) > k:
                    l = invalid.popleft() + 1

                max_len = max(max_len, r - l + 1)

        return max_len