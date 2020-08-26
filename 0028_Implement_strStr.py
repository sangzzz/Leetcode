class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n > h:
            return -1
        elif n == h and haystack != needle:
            return -1
        for i in range(0, h-n+1):
            x = haystack[i:i+n]
            if x == needle:
                return i
        return -1
