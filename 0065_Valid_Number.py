class Solution:
    def isNumber(self, st: str) -> bool:
        def work(s, e, sign):
            if (e or sign) and ' ' in s:
                return False
            s = s.strip()
            # print(s)
            if s == "":
                return False
            if s == '.':
                return False
            if s[0] == 'e' or s[-1] == 'e':
                return False
            if s == '+' or s == '-':
                return False
            numStart = False
            dec = False
            nums = [str(i) for i in range(10)]
            for j, i in enumerate(s):
                if not sign and i in {'+', '-'}:
                    sign = True
                    if j == 0:
                        return work(s[j+1:], e, True)
                    else:
                        return False
                elif not e and not dec and i == '.':
                    dec = True
                elif e == False and i == 'e':
                    if not numStart:
                        return False
                    # print(s[j+1:])
                    return work(s[j+1:], True, False)
                elif i in nums:
                    numStart = True
                    continue
                else:
                    return False
            return True

        return work(st, False, False)
