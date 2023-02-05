class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], index]
            hash_map[num] = index
