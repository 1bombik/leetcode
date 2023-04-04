# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        sentence = set(sentence)
        for i in alphabet:
            if i not in sentence:
                return False
        return True
