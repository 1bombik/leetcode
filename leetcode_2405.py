# https://leetcode.com/problems/optimal-partition-of-string/description/

class Solution:
    def partitionString(self, s: str) -> int:
        step = 0
        answer = 1
        s_len = len(s) - 1
        substr = ''
        while step <= s_len:
            if s[step] in substr:
                answer += 1
                substr = ''
            substr += s[step]
            step += 1
        return answer
