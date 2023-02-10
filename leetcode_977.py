# https://leetcode.com/problems/squares-of-a-sorted-array/?envType=study-plan&id=algorithm-i

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i * i for i in nums])
