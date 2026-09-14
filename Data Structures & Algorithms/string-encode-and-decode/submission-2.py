class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for ss in strs:
            s+=(ss)
            s+=("gabu8yuga")
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        strs = list()
        strs = s.split("gabu8yuga")
        strs.pop()
        return strs