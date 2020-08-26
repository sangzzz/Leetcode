class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        T = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
            'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        sol = []
        if digits == "":
            return []

        def permute(d, s):
            if len(s) == len(digits):
                sol.append(s)
            try:
                x = T[d[0]]
                for i in x:
                    try:
                        permute(d[1:], s+i)
                    except:
                        pass
            except:
                pass
        permute(digits, "")
        return sol
