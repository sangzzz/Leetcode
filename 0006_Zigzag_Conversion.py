class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        c = 1
        x = ""
        flag = 1
        order = []
        for i in s:
            order.append(c)
            if flag == 1:
                c = c+1
            else:
                c = c-1
            if c == numRows:
                flag = 0
            if c == 1:
                flag = 1
        i = 1
        wordList = ['' for i in range(0, numRows)]
        for index in range(0, len(s)):
            wordList[order[index]-1] += s[index]
        x = ''.join(wordList)
        return x
