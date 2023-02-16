# ttps://leetcode.com/problems/sqrtx/description/

from math import sqrt, trunc


class Solution:
    def mySqrt(self, x: int) -> int:
        return trunc(int(sqrt(x)))
