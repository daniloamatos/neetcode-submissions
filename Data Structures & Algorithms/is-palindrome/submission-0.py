class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (c := ''.join(ch.lower() for ch in s if ch.isalnum())) == c[::-1]