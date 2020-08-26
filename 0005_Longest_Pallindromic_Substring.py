class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s = ""
        if len(s) == 0:
            return ""
        for i in range(0, len(s)):
            if len(max_s) > (len(s)-i):
                break
            for j in range(i+1, len(s)):
                # if len(max_s)>(len(s)-j):
                #     break
                x = s[i:j+1]
                if x == x[::-1] and len(x) > len(max_s):
                    max_s = x
        if max_s == "":
            return s[0]
        return max_s
