# https://leetcode.com/problems/first-bad-version/description/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            check = (start + end) // 2
            if isBadVersion(check) == False and isBadVersion(check + 1) == True:
                return check + 1
            if isBadVersion(check) == False and isBadVersion(check + 1) == False:
                start = check
            elif isBadVersion(check) == True and isBadVersion(check + 1) == True:
                end = check
