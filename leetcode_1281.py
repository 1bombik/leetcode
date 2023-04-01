# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        number = [int(i) for i in str(n)]
        prod = number[0]
        for i in number[1:]:
            prod *= i
        return prod - sum(number)
