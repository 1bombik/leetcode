# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        if s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        else:
            sign = 1

        result, i = 0, 0

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -2 ** 31:
            return -2 ** 31
        else:
            return result
