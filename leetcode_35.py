# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            check = (start + end) // 2
            if nums[check] == target:
                return check
            elif nums[check] < target:
                start = check + 1
            else:
                end = check - 1
        return start
