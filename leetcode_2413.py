# https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return min([i for i in range(1, 2 * n + 1) if i % 2 == 0 and i % n == 0])
