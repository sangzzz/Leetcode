class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def par(i):
            if i == 1:
                return ['()']
            x = par(i-1)
            s = []

            output = set()
            for str in x:
                output.add("()" + str)
                for i in range(len(str)):
                    new_str = str[:i] + "(" + str[i] + ")" + str[i+1:]
                    output.add(new_str)
                output.add("(" + str + ")")
                output.add(str + "()")
            return list(output)
        s = par(n)
        return s
