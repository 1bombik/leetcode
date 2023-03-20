# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        answer = 0
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        i = 1
        while i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                answer += 1
                i += 2
            else:
                i += 1
        if answer >= n:
            return True
        else:
            return False
