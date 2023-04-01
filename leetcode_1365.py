# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        answer = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            answer.append(count)
        return answer
