# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            while '()' in s or '[]' in s or "{}" in s:
                s = s.replace('()', '')
                s = s.replace('{}', '')
                s = s.replace('[]', '')
            if len(s) > 0:
                return False
            else:
                return True
