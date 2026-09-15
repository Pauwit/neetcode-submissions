class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        index = 0
        length = len(s)

        if s[length - 1] == '1':
            return False

        while index < length - 1:
            jump = min(index + maxJump, length - 1)
            if jump != length - 1 and jump > length - 1 - minJump:
                jump = length - 1 - minJump
            while jump >= index + minJump and s[jump] != '0':
                jump -= 1

            if jump < index + minJump:
                return False

            index = jump

        return True
        