# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''.join(map(str, digits))
        nums = int(nums) + 1
        answer = [int(i) for i in str(nums)]
        return answer
