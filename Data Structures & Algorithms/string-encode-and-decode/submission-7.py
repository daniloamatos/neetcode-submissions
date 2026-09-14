import uuid
class Solution:
    DELIM = str(uuid.uuid4())
    def encode(self, strs: List[str]) -> str:
        return self.DELIM.join(strs) + self.DELIM if strs else ""

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.split(self.DELIM)[:-1]