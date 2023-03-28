# https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        return [abs(a - b) for a, b in zip([sum(nums[:i]) for i in range(len(nums))],
                                           [sum(nums[i + 1:]) for i in range(len(nums))])]
