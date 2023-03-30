# https://leetcode.com/problems/sort-integers-by-the-power-value/description/

class Solution:
    def getKth(self, lo: int, hi: int, k: int):
        answers_dict = {}
        for i in range(lo, hi + 1):
            count = 0
            check = i
            while check != 1:
                if check % 2 == 0:
                    check = check / 2
                    count += 1
                else:
                    check = 3 * check + 1
                    count += 1
            answers_dict[i] = count
        sorted_dict = dict(sorted(answers_dict.items(), key=lambda item: item[1]))
        i = 0
        for key in sorted_dict.keys():
            i += 1
            if i == k:
                return key

