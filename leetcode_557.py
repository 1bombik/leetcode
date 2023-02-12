# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/?envType=study-plan&id=algorithm-i

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())
