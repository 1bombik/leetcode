class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_nums = [i for i in nums if i % 2 == 0]
        answer = 0
        if len(even_nums) < 1:
            return -1
        else:
            uniq_even_nums = sorted(list(set(even_nums)))
            print(uniq_even_nums)
            current_max_count = 0
            for i in uniq_even_nums:
                check = even_nums.count(i)
                if check > current_max_count:
                    current_max_count = check
                    answer = i
        return answer
