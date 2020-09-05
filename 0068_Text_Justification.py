class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def check(x):
            l = 0
            for i in x:
                l = l + len(i)
            if l == maxWidth:
                return True
            else:
                return False

        def justify(x):
            l = len(x) - 1
            if len(" ".join(x)) == maxWidth:
                return " ".join(x)
            for i in range(l):
                x[i] += ' '
            while True:
                for i in range(l):
                    x[i] += ' '

                    if check(x):
                        break
                if check(x):
                    break
            string = ""
            for i in x:
                string += i
            return string

        def left_justify(x):
            s = " ".join(x)
            while len(s) < maxWidth:
                s = s + ' '
            return s

        x = []
        xl = 0
        res = []
        for i in words:
            if xl + len(i) + len(x) <= maxWidth:
                x.append(i)
                xl += len(i)
            else:
                # s = " ".join(x)
                if len(x) == 1:
                    s = left_justify(x)
                else:
                    s = justify(x)
                res.append(s)
                xl = len(i)
                x = [i]

        s = left_justify(x)
        res.append(s)
        return res
