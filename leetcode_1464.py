# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        a = nums[-1] - 1
        b = nums[-2] - 1
        return a * b
