# https://leetcode.com/problems/sign-of-the-product-of-an-array/

from functools import reduce


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = reduce(lambda x, y: x * y, nums)
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
