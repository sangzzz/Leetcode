class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def myfunct(e):
            return len(e)
        strs.sort(key=myfunct)
        if len(strs) == 0:
            return ""
        x = strs[0]
        while len(x) != 0:
            l = len(x)
            for i in strs:
                if i[0:l] != x:
                    x = x[0:-1]
                    break
            if len(x) == l:
                break
        return x
