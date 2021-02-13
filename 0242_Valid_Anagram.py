class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in range(len(s)):
            try:
                map[s[i]] += 1
            except:
                map[s[i]] = 1
        for i in range(len(t)):
            try:
                map[t[i]] -= 1
            except:
                map[t[i]] = -1
        for i in map:
            if map[i] != 0:
                return False
        return True