class Solution:
    def nextAlphaNum(self, s: str, i: int):
        i += 1
        while i < len(s) and not s[i].isalnum():
            i += 1

        return i

    def previousAlphaNum(self, s: str, i: int):
        i -= 1
        while i > 0 and not s[i].isalnum():
            i -= 1

        return i

    def isPalindrome(self, s: str) -> bool:
        i = self.nextAlphaNum(s, -1)
        j = self.previousAlphaNum(s, len(s))

        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i = self.nextAlphaNum(s, i)
            j = self.previousAlphaNum(s, j)
        
        return True
        