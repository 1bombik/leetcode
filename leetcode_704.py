# https://leetcode.com/problems/binary-search/description/?envType=study-plan&id=algorithm-i

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            check = nums[mid]
            if check == target:
                return mid
            if check > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
