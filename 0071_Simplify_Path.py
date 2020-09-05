class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        while '' in s:
            s.remove('')
        res = []
        for i in s:
            if i == '.':
                continue
            if i == '..':
                try:
                    res = res[0:-1]
                except:
                    res = []
            else:
                res.append(i)
        # print(s)
        return "/"+"/".join(res)
