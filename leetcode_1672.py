# https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(i) for i in accounts])
