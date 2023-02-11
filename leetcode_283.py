# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan&id=algorithm-i

class Solution:
    def moveZeroes(self, nums: list[int]):
        zeros = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for i in range(zeros):
            nums.append(0)
        return nums


res = Solution.moveZeroes('', nums=[0, 1, 0, 3, 12])
print(res)
