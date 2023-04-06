# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums)[-k]
