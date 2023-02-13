# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0 and high % 2 != 0:
            return int((high - low) / 2 + 1)
        elif low % 2 == 0 and high % 2 == 0:
            return int((high - low) / 2)
        else:
            return int(round(high - low + 1) / 2)
