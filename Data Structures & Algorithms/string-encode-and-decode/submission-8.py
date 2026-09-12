class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "//p0"

        ret = ""
        for s in strs:
            ret += s + "//pw"
        return ret[:-4]
        

    def decode(self, s: str) -> List[str]:
        if s == "//p0":
            return []

        ret = s.split("//pw")

        return ret
