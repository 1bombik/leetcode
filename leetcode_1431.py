# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        answer = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            if max(candies) == candies[i]:
                answer.append(True)
            else:
                answer.append(False)
            candies[i] -= extraCandies
        return answer
