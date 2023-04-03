# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/

class Solution:
    def countDigits(self, num: int) -> int:
        answer = 0
        nums = [int(i) for i in str(num)]
        for i in nums:
            if num % i == 0:
                answer += 1
        return answer
