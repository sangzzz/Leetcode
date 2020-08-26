class Solution:
    def countAndSay(self, n: int) -> str:
        T = {}
        T[1] = "1"

        def find(string):
            prev = string[0]
            res = ""
            cnt = 1
            for i in string[1:]:
                if i != prev:
                    res = res + str(cnt) + str(prev)
                    cnt = 1
                else:
                    cnt += 1
                prev = i
            res = res + str(cnt) + str(prev)
            return res

        for i in range(2, n+1):
            T[i] = find(T[i-1])
        return T[n]
