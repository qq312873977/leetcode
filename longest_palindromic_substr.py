class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1 or s == s[::-1]:
            return s
        max_len = 1
        #res = s[0] if s else ''
        start = 0
        for idx, ch in enumerate(s):
            left = idx - (max_len + 1) / 2
            right = idx + (max_len + 1) / 2
            if s[left+1:right] == s[right-1:left:-1]:
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        if max_len < right - left + 1:
                            max_len = right - left + 1
                            #res = s[left:right+1]
                            start = left
                        left -= 1
                        right += 1
                    else:
                        break

            if idx < len(s) - 1 and s[idx] == s[idx+1]:
                if max_len < 2:
                    #res = s[idx:idx+2]
                    start = idx
                    max_len = 2
                left = idx - max_len / 2
                right = idx + max_len / 2 + 1
                if s[left+1:right] == s[right-1:left:-1]:
                    while left >= 0 and right < len(s):
                        if s[left] == s[right]:
                            if max_len < right - left + 1:
                                max_len = right - left + 1
                                start = left
                                #res = s[left:right+1]
                            left -= 1
                            right += 1
                        else:
                            break
        return s[start:start+max_len]

    def longestPalindrome_2(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s
        if s == s[::-1]:
            return s

        maxLen, start = 1, 0

        for i in range(l):
            odd = s[i - maxLen - 1:i + 1]
            even = s[i - maxLen:i + 1]
            if i - maxLen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and even == even[::-1]:
                start = i - maxLen
                maxLen += 1

        return s[start:start + maxLen]

print Solution().longestPalindrome('abdeded')