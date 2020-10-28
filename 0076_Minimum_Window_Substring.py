class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = {}
        left = 0
        right = 0
        for i in t:
            try:
                T[i] += 1
            except:
                T[i] = 1
        S = {}
        for i in T:
            S[i] = -T[i]
        min_window = s
        min_window_length = len(s) + 1
        formed = 0
        required = len(T)
        while right < len(s):
            try:
                S[s[right]] += 1
                if S[s[right]] == 0:
                    formed += 1
                while left <= right and formed == required:
                    if right-left+1 < min_window_length:
                        min_window_length = right - left + 1
                        min_window = s[left: right+1]
                    try:
                        S[s[left]] -= 1
                        if S[s[left]] < 0:
                            formed -= 1
                    except:
                        left += 1
                        continue
                    left += 1
                right += 1
            except:
                right += 1
                continue
        return "" if min_window_length == len(s) + 1 else min_window
