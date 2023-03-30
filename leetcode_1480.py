# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        answer = []
        current_summ = 0
        for i in nums:
            current_summ += i
            answer.append(current_summ)
        return answer
