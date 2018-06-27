class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_len = 1
        begin = 0
        end = 1
        while end < len(s):
            tmp_s = s[begin:end]
            if s[end] in tmp_s:
                max_len = max(max_len, end - begin)
                begin += tmp_s.index(s[end]) + 1
            end += 1
        max_len = max(max_len, end - begin)
        return max_len

    def lengthOfLongestSubstring_2(self, s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length

print Solution().lengthOfLongestSubstring_2('abcddddd')