# https://leetcode.com/problems/rotate-array/description/?envType=study-plan&id=algorithm-i

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        while i < k:
            nums.insert(0, nums[-1])
            nums.pop(-1)
            i += 1
        return nums
