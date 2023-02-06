class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        char_set = {set()}
        max_len = 0
        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                char_set.remove(s[start])
                start += 1
        return max_len

