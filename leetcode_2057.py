# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        i = 0
        while i <= len(nums) - 1:
            if i % 10 == nums[i]:
                return i
            else:
                i += 1
        return -1