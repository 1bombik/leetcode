# https://leetcode.com/problems/reducing-dishes/description/

class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort(reverse=True)
        answer = 0
        presum = 0
        for i in range(len(satisfaction)):
            presum += satisfaction[i]
            if presum < 0:
                break
            answer += presum
        return answer
