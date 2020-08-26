class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = ""
        l = 0
        for i in s:
            if i not in x:
                x = x+i
            else:
                pos = x.find(i)
                if len(x) == 0:
                    x = i
                else:
                    x = x[pos+1:] + i
            if len(x) > l:
                l = len(x)
        return l
