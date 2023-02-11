# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan&id=algorithm-i

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(numbers):
            if target - num in hash_map:
                return [hash_map[target - num] + 1, index + 1]
            hash_map[num] = index
