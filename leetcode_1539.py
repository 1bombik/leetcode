# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing_nums = []
        k_copy = 0
        times = 1
        while k_copy <= k:
            if times not in arr:
                missing_nums.append(times)
                k_copy += 1
            times += 1
        return missing_nums[k - 1]
