# https://leetcode.com/problems/add-to-array-form-of-integer/description/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = ''.join(map(str, num))
        sum = int(nums) + k
        answer = [int(i) for i in str(sum)]
        return answer
