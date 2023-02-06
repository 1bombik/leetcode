# https://leetcode.com/problems/shuffle-the-array/description/

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        answer = []
        for i in range(0, int(len(nums)/2)):
            answer.append(nums[i])
            answer.append(nums[i+n])
        return answer
