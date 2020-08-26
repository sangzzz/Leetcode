class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.split(' ')
        while '' in str:
            str.remove('')
        if len(str) == 0:
            return 0

        flag = "+"
        if str[0][0] == '+' or str[0][0] == '-':
            if len(str[0]) == 1:
                if str[0][0].isnumeric():
                    return int(str[0][0])
                else:
                    return 0
            flag = str[0][0]
            str[0] = str[0][1:]
        x = 0
        for i in str[0]:
            if i >= '0' and i <= '9':
                x = x+1
                continue
            else:
                break
        if flag == "+" and x > 0:
            if int(str[0][0:x]) > (2**31-1):
                return (2**31 - 1)
            return int(str[0][0:x])
        elif flag == "-" and x > 0:
            if int(str[0][0:x]) > (2**31):
                return -(2**31)
            return -int(str[0][0:x])
        if x == 0:
            return 0
