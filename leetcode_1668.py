# https://leetcode.com/problems/maximum-repeating-substring/description/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        word_copy = word
        answer = 0
        while True:
            if word in sequence:
                answer += 1
                word += word_copy
            else:
                return answer
