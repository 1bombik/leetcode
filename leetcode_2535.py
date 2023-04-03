# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        el_sum = sum(nums)
        dig_sum = ''.join(map(str, nums))
        for i in dig_sum:
            el_sum -= int(i)
        return el_sum
