# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max([i.count(' ') + 1 for i in sentences])
