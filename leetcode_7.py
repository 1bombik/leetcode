# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        check = 2 ** 31 - 1
        if x < 0:
            x = -x
            x = str(x)
            x = x[::-1]
            x = int(x)
            x = -x
            if x > -check:
                return x
            else:
                return 0
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x < check:
                return x
            else:
                return 0
