# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    answer += 1
        return answer
