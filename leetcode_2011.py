# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        answer = 0
        for i in operations:
            if i == "--X" or i == "X--":
                answer -= 1
            else:
                answer += 1
        return answer
