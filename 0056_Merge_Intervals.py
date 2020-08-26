class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []
        pts = []
        for i in intervals:
            pts.append((i[0], 0))
            pts.append((i[1], 1))
        pts.sort()
        stack = []
        for i in pts:
            if i[1] == 0:
                stack.append(i[0])
            else:
                if len(stack) == 1:
                    sol.append([stack[0], i[0]])
                stack = stack[0:-1]
        return sol
