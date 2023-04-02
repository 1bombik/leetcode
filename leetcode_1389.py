# https://leetcode.com/problems/create-target-array-in-the-given-order/description/

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        answer = []
        for i in range(len(nums)):
            answer.insert(index[i], nums[i])
        return answer
