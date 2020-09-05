class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r = len(word2) + 1
        c = len(word1) + 1
        T = [[0 for i in range(0, c)] for j in range(0, r)]
        for i in range(0, r):
            T[i][0] = i
        for i in range(0, c):
            T[0][i] = i

        for i in range(1, r):
            for j in range(1, c):
                # insert = T[i-1][j] + 1
                # delete = T[i][j-1] + 1
                # mismatch = T[i-1][j-1] + 1
                # match = T[i-1][j-1]

                if word1[j-1] == word2[i-1]:
                    # T[i][j] = min(match, delete, insert)
                    T[i][j] = min(T[i-1][j-1], T[i-1][j] + 1, T[i][j-1]+1)
                else:
                    # T[i][j] = min(mismatch, delete, insert)
                    T[i][j] = min(T[i-1][j-1], T[i-1][j], T[i][j-1]) + 1

        # print(T)
        return T[-1][-1]
