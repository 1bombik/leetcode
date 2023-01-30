# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        merged_array = sorted(merged_array)
        if len(merged_array) % 2 == 0:
            answer = (merged_array[int(len(merged_array) / 2 - 1)] + merged_array[int(len(merged_array) / 2)]) / 2
        else:
            answer = merged_array[int((len(merged_array) - 1) / 2)]
        return answer
